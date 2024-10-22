from global_variables import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from plotly.graph_objs import Figure, Scatter, Layout
import panel as pn

# Useful Functions


def prompt_monthly_cost(month, cost):
    coefficient = month//12
    monthly_cost = cost * (1 + get_monthly_interest_rate()) ** coefficient
    return monthly_cost


def cloud_storage_monthly_cost(month):
    coefficient = month//12
    monthly_cost = db_cost * (1 + cloud_storage_costs_growth) ** coefficient
    return monthly_cost

# Month user growth


def month_users(initial_users, annual_growth, months):

    # Base user, if 0 return the initial number of users
    if months == 0:
        return initial_users

    # Monthly growth
    monthly_growth = annual_growth / 12

    # Previous month users
    previous_month_users = month_users(
        initial_users, annual_growth, months - 1)

    # Current month growth
    current_month_growth = previous_month_users * monthly_growth
    current_month_users = previous_month_users + current_month_growth

    return current_month_users

# Month contacts growth


def month_contacts(initial_contacts, annual_growth, months):

    # Base user, if 0 return the initial number of users
    if months == 0:
        return initial_contacts

    # Monthly growth
    monthly_growth = annual_growth / 12

    # Previous month users
    previous_month_contacts = month_contacts(
        initial_contacts, annual_growth, months - 1)

    # Current month growth
    current_month_growth = previous_month_contacts * monthly_growth
    current_month_contacts = previous_month_contacts + current_month_growth
    return current_month_contacts

# Minutes Call Center Growth


def month_minutes(initial_minutes, annual_growth, months):

    # Base user, if 0 return the initial number of users
    if months == 0:
        return initial_minutes

    # Monthly growth
    monthly_growth = annual_growth / 12

    # Previous month users
    previous_month_minutes = month_contacts(
        initial_minutes, annual_growth, months - 1)

    # Current month growth
    current_month_growth = previous_month_minutes * monthly_growth
    current_month_minutes = previous_month_minutes + current_month_growth
    return current_month_minutes

# First Implementation: GPT 4


def calculate_vpn_gpt4(months, discount_rate):
    """
    Calculates the Net Present Value (VPN) of the GPT-4 investment.

    Args:
      months_range: Range of months to consider.
      discount_rate: The discount rate (e.g., 0.05 for 5%) (monthly).

    Returns:
      The calculated VPN.
    """

    vpn = 0
    gpt4_initial_investment = - \
        (dolar * enginner_cost * comercial_implementation_time)  # only developlment

    for month in range(1, months + 1):
        # Cost interaction
        total_contacts_month = ((month_contacts(contacts_per_month, contacts_annual_growth, month))
                                + ((month_users(get_active_users(), users_annual_growth, month)-get_active_users())*users_that_contact_ratio*avg_contacts_per_user))

        cost_interactions_gpt4 = -(total_contacts_month * get_cost_prompt_gpt4_cop()) * (
            # interactions * increase in cost
            (1+api_costs_growth)**(month//12))

        # Cost storage
        cost_storage_gpt4 = - \
            cloud_storage_monthly_cost(
                month) * dolar * ((1+cloud_storage_costs_growth)**(month//12))

        # Total monthly cost
        total_cost = cost_interactions_gpt4 + cost_storage_gpt4

        # Discount the cash flow
        discounted_cost = total_cost / (1 + discount_rate) ** month

        # Add the discounted cost to the VPN
        vpn += discounted_cost

    # Add the initial investment (as a negative cash flow)
    vpn += gpt4_initial_investment

    return vpn

# Second Implementation: GPT3.5


def calculate_vpn_gpt3(months, discount_rate):
    """
    Calculates the Net Present Value (VPN) of the GPT-3 investment
    """
    vpn = 0
    gpt3_initial_investment = - \
        (dolar * enginner_cost * comercial_implementation_time)

    for month in range(1, months + 1):
        # Cost interaction
        total_contacts_month = ((month_contacts(contacts_per_month, contacts_annual_growth, month))
                                + ((month_users(get_active_users(), users_annual_growth, month)-get_active_users())*users_that_contact_ratio*avg_contacts_per_user))

        cost_interactions_gpt3 = -(total_contacts_month * cost_prompt_gpt3_cop) * (
            # interactions * increase in cost
            (1+api_costs_growth)**(month//12))

        # Cost storage
        cost_storage_gpt3 = - \
            cloud_storage_monthly_cost(
                month) * dolar * ((1+cloud_storage_costs_growth)**(month//12))

        # Total monthly cost
        total_cost = cost_interactions_gpt3 + cost_storage_gpt3

        # Discount the cash flow
        discounted_cost = total_cost / (1 + discount_rate) ** month

        # Add the discounted cost to the VPN
        vpn += discounted_cost

    # Add the initial investment (as a negative cash flow)
    vpn += gpt3_initial_investment

    return vpn

# Third Implementation: Local


def calculate_vpn_native(months, discount_rate):
    """
    Calculates the Net Present Value (VPN) of the GPT-3 investment
    """
    vpn = 0
    native_initial_investment = - \
        (dolar * enginner_cost * native_implementation_time)

    for month in range(1, months + 1):
        # Cost interaction
        cost_interactions_native = - \
            (gpu_cost * dolar * 24 * (365/12)) * \
            ((1-cloud_processing_costs_decline)**(month//12))

        # Cost storage
        cost_storage_native = - \
            cloud_storage_monthly_cost(
                month) * dolar * ((1+cloud_storage_costs_growth)**(month//12))

        # Total monthly cost
        total_cost = cost_interactions_native + cost_storage_native

        # Discount the cash flow
        discounted_cost = total_cost / (1 + discount_rate) ** month

        # Add the discounted cost to the VPN
        vpn += discounted_cost

    # Add the initial investment (as a negative cash flow)
    vpn += native_initial_investment

    return vpn

# Base Implementation: Call Center


def calculate_vpn_callcenter(months, discount_rate):
    vpn = 0
    for month in range(1, months + 1):
        # Costs Infraestructure
        call_center_outbound_cost = month_minutes(
            dialogue_minutes_monthly_avg, users_annual_growth, month) * minute_cost * dolar
        infraestructure_cost = -(get_call_center_license_cost() + get_call_center_line_cost() +
                                 call_center_outbound_cost)*((1+callcenter_costs_growth)**(month//12))

        # Cost interaction
        assistants_cost = -(get_call_center_assistants_cost()) * \
            ((1+salary_growth)**(month//12))

        # Total monthly cost
        total_cost = infraestructure_cost + assistants_cost

        # Discount the cash flow
        discounted_cost = total_cost / (1 + discount_rate) ** month

        # Add the discounted cost to the VPN
        vpn += discounted_cost

    return vpn

# Month where VPNs are equal function


def find_equal_vpn_month(months_range, discount_rate):
    """
    Finds the month where the VPNs from the three scenarios are equal.

    Args:
        months_range: A range of months to consider.
        discount_rate: The discount rate for calculating VPN.

    Returns:
        The month where the VPNs are equal, or None if no such month exists.
    """

    # Calculate VPNs for each scenario for all months
    vpns = {
        "native": [calculate_vpn_native(month, discount_rate) for month in range(1, months_range + 1)],
        "commercial": [calculate_vpn_gpt4(month, discount_rate) for month in range(1, months_range + 1)],
    }

    # Find the month where the VPNs are closest to being equal
    equal_month = None
    min_difference = float('inf')
    for month, (native_vpn, commercial_vpn) in enumerate(zip(*vpns.values()), start=1):
        difference = abs(native_vpn - commercial_vpn)
        if difference < min_difference:
            equal_month = month
            min_difference = difference

    return equal_month


def graph_vpns_and_equality(months_range, discount_rate):
    """
    Graphs the VPNs for three scenarios and marks the point of equality (optional).

    Args:
        months_range: A range of months to consider.
        discount_rate: The discount rate for calculating VPN.
    """

    # Calculate VPNs for each scenario for all months
    vpns = {
        "native": [calculate_vpn_native(month, discount_rate) for month in range(1, months_range + 1)],
        "commercial": [calculate_vpn_gpt4(month, discount_rate) for month in range(1, months_range + 1)],
        "callcenter": [calculate_vpn_callcenter(month, discount_rate) for month in range(1, months_range + 1)],
    }

    # Find the month where the native and commercial VPNs are closest to being equal (optional)
    # equal_month = find_equal_vpn_month(months_range, discount_rate)

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, months_range + 1), vpns["native"], label="Native VPN")
    plt.plot(range(1, months_range + 1),
             vpns["commercial"], label="Commercial VPN")
    plt.plot(range(1, months_range + 1),
             vpns["callcenter"], label="Call Center VPN")  # Add the new line

    equal_month = None
    min_difference = float('inf')
    for month, vpn_values in enumerate(zip(*vpns.values()), start=1):
        native_vpn, commercial_vpn, callcenter_vpn = vpn_values
        difference = abs(native_vpn - commercial_vpn)
        if difference < min_difference:
            equal_month = month
            min_difference = difference

    # Mark the point of equality (optional)
    if equal_month:
        plt.scatter(equal_month, vpns["native"][equal_month - 1],
                    color='red', marker='x', label="Equal VPN Month")
        plt.text(equal_month, vpns["native"][equal_month -
                 1] + 10, f"Month {equal_month}", ha='center')

    # Set plot labels and title}
    plt.figure(figsize=(10, 6))
    plt.xlabel("Months")
    plt.ylabel("VPN")
    plt.title("Comparison of Native, Commercial, and Call Center VPNs")
    # Show the legend
    plt.legend()

    # Save the results
    plt.savefig('comparison_plot.png', bbox_inches='tight')
    # Display the plot
    plt.show()


def generate_plot(months_range, discount_rate):
    vpns = {
        "native": [calculate_vpn_native(month, discount_rate) for month in range(1, months_range + 1)],
        "commercial_4": [calculate_vpn_gpt4(month, discount_rate) for month in range(1, months_range + 1)],
        "commercial_3": [calculate_vpn_gpt3(month, discount_rate) for month in range(1, months_range + 1)],
        "callcenter": [calculate_vpn_callcenter(month, discount_rate) for month in range(1, months_range + 1)],
    }

    equal_month = None
    min_difference = float('inf')
    for month, vpn_values in enumerate(zip(*vpns.values()), start=1):
        native_vpn, commercial_4_vpn, commercial_3_vpn, callcenter_vpn = vpn_values
        difference = abs(native_vpn - commercial_4_vpn)
        if difference < min_difference:
            equal_month = month
            min_difference = difference

    # Create Plotly Figure
    fig = Figure()
    fig.add_trace(Scatter(x=list(range(1, months_range + 1)),
                  y=vpns["native"], name="VPN Nativo  (Zephyr7B)"))
    fig.add_trace(Scatter(x=list(range(1, months_range + 1)),
                  y=vpns["commercial_4"], name="VPN Comercial (GPT4)"))
    fig.add_trace(Scatter(x=list(range(1, months_range + 1)),
                  y=vpns["commercial_3"], name="VPN Comercial (GPT3.5)"))
    fig.add_trace(Scatter(x=list(range(1, months_range + 1)),
                  y=vpns["callcenter"], name="Call Center VPN"))

    if equal_month:
        fig.add_trace(Scatter(x=[equal_month], y=[vpns["native"][equal_month - 1]], mode='markers',
                      marker=dict(color='red', size=10, symbol='x'), name="Mes VPN Igual"))
        fig.add_annotation(
            x=equal_month, y=vpns["native"][equal_month - 1] + 10, text=f"Mes {equal_month}", showarrow=False)

    fig.update_layout(
        title="Comparación VPNs Nativo, Comercial (GPT4) y Call Center",
        title_x=0.5,
        xaxis_title="Months",
        yaxis_title="VPN",
        legend_title="VPN Scenarios"
    )

    return fig
