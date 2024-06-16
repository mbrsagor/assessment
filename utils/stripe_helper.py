import stripe

stripe.api_key = 'stripe_api_key'

customer = stripe.Customer.create(
    idempotency_key='KG5LxwFBepaKHyUSD',
    name='Bozlur Rosid Sagor', email='mbrsagor@gmail.com',
    phone='123456789', address='Dhaka'
)
print(customer)
