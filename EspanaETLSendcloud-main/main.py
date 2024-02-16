import requests

# Replace 'your_sendcloud_public_key' and 'your_sendcloud_private_key' with your actual API keys
public_key = "a9d5ffb6-c990-425b-93c1-15fcb675d1f8"
private_key = "2425c2b13b744e29960b903f3329fd13"

response = requests.get('https://panel.sendcloud.sc/api/v2/parcels', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/parcels/{id}', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/parcels/{id}/return_portal_url', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/parcels/statuses', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/parcels/{id}/documents/{type}', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/labels/{parcel_id}', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/labels/normal_printer/{parcel_id}', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/labels/normal_printer', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/labels/label_printer/{parcel_id}', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/labels/label_printer', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/customs_declaration/normal_printer/{parcel_id}', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/customs_declaration/normal_printer', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/pickups/{id}', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/pickups', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/shipping_methods', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/shipping_methods/{id}', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/shipping-products', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/shipping-functionalities', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/shipping-price', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/insights/carriers/transit-times', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/insights/shipping-methods/transit-times', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/user/addresses/sender', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/user/addresses/sender/{id}', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/contracts', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/contracts/{id}', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/checkout/configurations/{configuration_id}/delivery-options', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/tracking/{tracking_number}', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/returns', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/returns/{id}', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/brand/{brand_domain}/return-portal', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/brand/{brand_domain}/return-portal/outgoing', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/brand/{brand_domain}/return-portal/label/polling', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/brand/{brand_domain}/return-portal/label/download', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/brand/{brand_domain}/return-portal', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/brand/{brand_domain}/return-portal/outgoing', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/brand/{brand_domain}/return-portal/label/polling', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/brand/{brand_domain}/return-portal/label/download', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/integrations', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/integrations/{id}', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/integrations/logs', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/integrations/{id}/logs', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/integrations/{id}/shipments', auth=(public_key, private_key))
response = requests.get('https://servicepoints.sendcloud.sc/api/v2/service-points', auth=(public_key, private_key))
response = requests.get('https://servicepoints.sendcloud.sc/api/v2/service-points/{service_point_id}', auth=(public_key, private_key))
response = requests.get('https://servicepoints.sendcloud.sc/api/v2/service-points/{service_point_id}/check-availability', auth=(public_key, private_key))
response = requests.get('https://servicepoints.sendcloud.sc/api/v2/carriers', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/brands', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/brands/{id}', auth=(public_key, private_key))
response = requests.get('https://servicepoints.sendcloud.sc/api/v2/service-points', auth=(public_key, private_key))
response = requests.get('https://servicepoints.sendcloud.sc/api/v2/service-points/{service_point_id}', auth=(public_key, private_key))
response = requests.get('https://servicepoints.sendcloud.sc/api/v2/service-points/{service_point_id}/check-availability', auth=(public_key, private_key))
response = requests.get('https://servicepoints.sendcloud.sc/api/v2/carriers', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/brands', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/brands/{id}', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/user/invoices', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/user/invoices/{id}', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/reporting/parcels/{report_id}', auth=(public_key, private_key))
response = requests.get('https://panel.sendcloud.sc/api/v2/user', auth=(public_key, private_key))

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error al realizar la solicitud:", response.status_code)

breakpoint()
