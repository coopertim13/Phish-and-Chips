import EmailTemplate
from email.mime.image import MIMEImage

class LinkedIn(EmailTemplate.EmailTemplate):
	def __init__(self, email, full_name, first_name, record, sender_name, recipient):
		super().__init__(email, full_name, first_name, record, sender_name, recipient, content, "LinkedIn Security Alert")
	
	def build(self):
		msg = super().build()

		fp = open('linkedin/linkedin.png', 'rb')
		msgImage = MIMEImage(fp.read())
		fp.close()

		msgImage.add_header('Content-ID', '<logo>')
		msg.attach(msgImage)

		return msg

content = """
  <html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="content-type" content="text/html; charset=utf-8">
  	<meta name="viewport" content="width=device-width, initial-scale=1.0;">
 	<meta name="format-detection" content="telephone=no"/>
	<style>
/* Reset styles */ 
body {{ margin: 0; padding: 0; min-width: 100%; width: 100% !important; height: 100% !important;}}
body, table, td, div, p, a {{ -webkit-font-smoothing: antialiased; text-size-adjust: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; line-height: 100%; }}
table, td {{ mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-collapse: collapse !important; border-spacing: 0; }}
img {{ border: 0; line-height: 100%; outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; }}
#outlook a {{ padding: 0; }}
.ReadMsgBody {{ width: 100%; }} .ExternalClass {{ width: 100%; }}
.ExternalClass, .ExternalClass p, .ExternalClass span, .ExternalClass font, .ExternalClass td, .ExternalClass div {{ line-height: 100%; }}
/* Rounded corners for advanced mail clients only */ 
@media all and (min-width: 560px) {{
	.container {{ border-radius: 8px; -webkit-border-radius: 8px; -moz-border-radius: 8px; -khtml-border-radius: 8px;}}
}}
/* Set color for auto links (addresses, dates, etc.) */ 
a, a:hover {{
	color: #127DB3;
}}
.footer a, .footer a:hover {{
	color: #999999;
}}
 	</style>
	<!-- MESSAGE SUBJECT -->
	<title>LinkedIn Security Alert</title>
</head>
<!-- BODY -->
<!-- Set message background color (twice) and text color (twice) -->
<body topmargin="0" rightmargin="0" bottommargin="0" leftmargin="0" marginwidth="0" marginheight="0" width="100%" style="border-collapse: collapse; border-spacing: 0; margin: 0; padding: 0; width: 100%; height: 100%; -webkit-font-smoothing: antialiased; text-size-adjust: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; line-height: 100%;
	background-color: #F0F0F0;
	color: #000000;"
	bgcolor="#F0F0F0"
	text="#000000">
<!-- SECTION / BACKGROUND -->
<!-- Set message background color one again -->
<table width="100%" align="center" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse; border-spacing: 0; margin: 0; padding: 0; width: 100%;" class="background"><tr><td align="center" valign="top" style="border-collapse: collapse; border-spacing: 0; margin: 0; padding: 0;"
	bgcolor="#F0F0F0">
<!-- WRAPPER -->
<!-- Set wrapper width (twice) -->
<table border="0" cellpadding="0" cellspacing="0" align="center"
	width="560" style="border-collapse: collapse; border-spacing: 0; padding: 0; width: inherit;
	max-width: 560px;" class="wrapper">
	<tr>
		<td align="left" valign="top" style="border-collapse: collapse; border-spacing: 0; margin: 0; padding: 0; padding-left: 3.5%; padding-right: 6.25%; width: 87.5%;
			padding-top: 20px;
			padding-bottom: 20px;">
			<!-- PREHEADER -->
			<!-- Set text color to background color -->
			<div style="display: none; visibility: hidden; overflow: hidden; opacity: 0; font-size: 1px; line-height: 1px; height: 0; max-height: 0; max-width: 0;
			color: #F0F0F0;" class="preheader">
				Hi {first_name}, we noticed someone just tried to sign in to your LinkedIn account from a location you haven't used before, so we want to make sure it's really you.</div>
			<!-- LOGO -->
			<!-- Image text color should be opposite to background color. Set your url, image src, alt and title. Alt text should fit the image size. Real image size should be x2. URL format: http://domain.com/?utm_source={{Campaign-Source}}&utm_medium=email&utm_content=logo&utm_campaign={{Campaign-Name}} -->
			<a target="_blank" style="text-decoration: none;"
				href="#"><img border="0" vspace="0" hspace="0"
				src="cid:logo"
				width="40" height="33"
				alt="Logo" title="Logo" style="
				color: #000000;
				font-size: 10px; margin: 0; padding: 0; outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; border: none; display: block;" /></a>
      </td>
	</tr>
<!-- End of WRAPPER -->
</table>
<!-- WRAPPER / CONTEINER -->
<!-- Set conteiner background color -->
<table border="0" cellpadding="0" cellspacing="0" align="center"
	bgcolor="#FFFFFF"
	width="560" style="border-collapse: collapse; border-spacing: 0; padding: 0; width: inherit;
	max-width: 560px;" class="container">
	<!-- HEADER -->
	<!-- Set text color and font family ("sans-serif" or "Georgia, serif") -->
	<tr>
		<td valign="top" style="border-collapse: collapse; border-spacing: 0; margin: 0; padding: 0; padding-left: 3.5%; padding-right: 6.25%; width: 87.5%; font-size: 24px; font-weight: bold; line-height: 130%;
			padding-top: 25px;
			color: #000000;
			font-family: sans-serif;" class="header">
				Hi {first_name},
		</td>
	</tr>
	
	<!-- SUBHEADER -->
	<!-- Set text color and font family ("sans-serif" or "Georgia, serif") -->
	<tr>
		<td valign="top" style="border-collapse: collapse; border-spacing: 0; margin: 0; padding: 0; padding-bottom: 3px; padding-left: 3.5%; padding-right: 6.25%; width: 87.5%; font-size: 16px; font-weight: 300; line-height: 100%;
			padding-top: 5px;
			color: #000000;
			font-family: sans-serif;" class="subheader">
				We noticed someone just tried to sign in to your LinkedIn account from a location you haven’t used before, so we want to make sure it’s really you.
                <p></p><br/>
                <b>If you did try to sign in:</b><br/>
                Please use this verification code to complete your sign in: <b>437983</b>
                <p></p><br/>
                <b>If you didn't try to sign in, please change your password immediately.</b> You can do this by clicking the link below.
		</td>
	</tr>
 <!-- BUTTON -->
	<!-- Set button background color at TD, link/text color at A and TD, font family ("sans-serif" or "Georgia, serif") at TD. For verification codes add "letter-spacing: 5px;". Link format: http://domain.com/?utm_source={{Campaign-Source}}&utm_medium=email&utm_content={{Button-Name}}&utm_campaign={{Campaign-Name}} -->
	<tr>
		<td align="center" valign="top" style="border-collapse: collapse; border-spacing: 0; margin: 0; padding: 0; padding-left: 6.25%; padding-right: 6.25%; width: 87.5%;
			padding-top: 25px;
			padding-bottom: 5px;" class="button"><a
			href="https://www.yoururl.com" target="_blank" style="text-decoration: none;">
				<table border="0" cellpadding="0" cellspacing="0" align="center" style="max-width: 220px; min-width: 100px; border-collapse: collapse; border-spacing: 0; padding: 0;"><tr><td align="center" valign="middle" style="padding: 10px 20px; margin: 0; text-decoration: underline; border-collapse: collapse; border-spacing: 0; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; -khtml-border-radius: 4px;"
					bgcolor="#2867b2"><a target="_blank" style="text-decoration: none;
					color: #FFFFFF; font-family: sans-serif; font-size: 17px; font-weight: 400; line-height: 120%;"
					href="https://www.yoururl.com">
						Change Password
					</a>
			</td></tr></table></a><br/>
		</td>
	</tr>
		<tr>
		<td valign="top" style="border-collapse: collapse; border-spacing: 0; margin: 0; padding: 0; padding-bottom: 3px; padding-left: 3.5%; padding-right: 6.25%; width: 87.5%; font-size: 16px; font-weight: 300; line-height: 100%;
			padding-top: 5px;
			color: #000000;
			font-family: sans-serif;" class="subheader"><br/>
				Thanks for helping us keep your account secure.<br/>
                The LinkedIn Team<br/><p></p>
                <span style = "color: white;">.</span>
		</td>
	</tr>
<!-- End of WRAPPER -->
</table>
<table border="0" cellpadding="0" cellspacing="0" align="center"
	width="560" style="border-collapse: collapse; border-spacing: 0; padding: 0; width: inherit;
	max-width: 560px;" class="wrapper">
	<tr>
		<td bgcolor="#F7F7F7" valign="top" style="border-collapse: collapse; border-spacing: 0; margin: 0; padding: 0; padding-bottom: 3px; padding-left: 3.5%; padding-right: 6.25%; width: 87.5%; font-size: 16px; font-weight: 300; line-height: 100%;
			padding-top: 5px;
			color: #000000;
			font-family: sans-serif;" class="subheader"><br/>
				<b>When and where this happened</b>
                <span style="font-size:12px">
                <p></p><br/>
                <b>Date:</b><br/>
                April 28, 2021, 1:10 AM (GMT)
                <p></p><br/>
                <b>Operating System:</b><br/>
                Windows
                <p></p><br/>
                <b>Browser:</b><br/>
                Firefox
                <p></p><br/>
                <b>Approximate Location:</b><br/>
                Chatswood, New South Wales, Australia
                <p></p><br/>
                <b>Didn't do this?</b> Be sure to <a style = "text-decoration: none;" href = "https://www.yoururl.com">change your password</a> right away.<p></p>
                <span style="color: #F7F7F7">.</span>
                </span>
                <p></p><br/><p><p/>
		</td>
	</tr>
<!-- End of WRAPPER -->
</table>
<!-- WRAPPER -->
<!-- Set wrapper width (twice) -->
<table border="0" cellpadding="0" cellspacing="0" align="center"
	width="560" style="border-collapse: collapse; border-spacing: 0; padding: 0; width: inherit;
	max-width: 560px;" class="wrapper">
	<!-- SOCIAL NETWORKS -->
	<!-- Image text color should be opposite to background color. Set your url, image src, alt and title. Alt text should fit the image size. Real image size should be x2 -->
	<!-- FOOTER -->
	<!-- Set text color and font family ("sans-serif" or "Georgia, serif"). Duplicate all text styles in links, including line-height -->
	<tr>
		<td align="center" valign="top" style="border-collapse: collapse; border-spacing: 0; margin: 0; padding: 0; padding-left: 6.25%; padding-right: 6.25%; width: 87.5%; font-size: 12px; font-weight: 400; line-height: 100%;
			padding-top: 20px;
			padding-bottom: 20px;
			color: #999999;
			font-family: sans-serif;" class="footer">
				This email was intended for {full_name} (Director | Philanthropist at Fake Org Inc.).
                <p></p><br/>
                © 2021 LinkedIn Ireland Unlimited Company, Wilton Plaza, Wilton Place, Dublin 2. <br/>
                LinkedIn is a registered business name of LinkedIn Ireland Unlimited Company. <br/>
                LinkedIn and the LinkedIn logo are registered trademarks of LinkedIn.
		</td>
	</tr>
<!-- End of WRAPPER -->
</table>
<!-- End of SECTION / BACKGROUND -->
</td></tr></table>
</body>
</html>
"""