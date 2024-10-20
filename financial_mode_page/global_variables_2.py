# global_variables.py

# Fixed Variables

# Call Center
assistants = 9
salary = 1800000

# Costs OpenAI
gpt4_in_token = 0.00001
gpt4_out_token = 0.00003
gpt3_in_token = 0.0000005
gpt3_out_token = 0.0000015
emb_token = 0.0000001

# Local Model Costs
gpu_cost = 4.88  # per hour
db_cost = 50

# Use Case
active_users = 594000
contacts_per_month = 9345
dolar = 4300  # Remember to change to 3900
num_tokens_input = 800
num_tokens_output = 100
avg_interactions_per_contact = 5
enginner_cost = 75  # per hour
native_implementation_time = 20
comercial_implementation_time = 5

# Calculated Variables
cost_prompt_gpt4_usd = (num_tokens_input * gpt4_in_token) + \
    (num_tokens_output * gpt4_out_token)
cost_prompt_gpt4_cop = cost_prompt_gpt4_usd * \
    dolar * avg_interactions_per_contact
cost_prompt_gpt3_usd = (num_tokens_input * gpt3_in_token) + \
    (num_tokens_output * gpt3_out_token)
cost_prompt_gpt3_cop = cost_prompt_gpt3_usd * \
    dolar * avg_interactions_per_contact


# Callcenter Variables - Use getters for calculated values
dialogue_minutes_monthly_avg = 23144
minute_cost = 0.011765


line_cost = 36.47


def get_call_center_line_cost():
    return line_cost * dolar * assistants


software_license_cost = 68.6


def get_call_center_license_cost():
    return software_license_cost * dolar * assistants


def get_call_center_assistants_cost():
    return salary * assistants


# Scenery Parameters
contacts_annual_growth = 0.7


def get_contacts_monthly_growth():
    return (1 + contacts_annual_growth) ** (1 / 12) - 1


users_annual_growth = 0.1


def get_users_monthly_growth():
    return (1 + users_annual_growth) ** (1 / 12) - 1


annual_interest_rate = 0.1222


def get_monthly_interest_rate():
    return ((1 + annual_interest_rate) ** (1 / 12)) - 1


callcenter_costs_growth = 0.2
salary_growth = 0.10
cloud_storage_costs_growth = 0.1060
cloud_processing_costs_decline = 0.15
api_costs_growth = 0.05
users_that_contact_ratio = 0.0076
avg_contacts_per_user = 2.07


# Financial Model Parameters
model_months = 60
