from plyer import notification

def notifyMe(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = r"C:\Users\Us\Desktop\Python Files\Python_logo_for_notification.ico",
        timeout = 6
    )

_name_ = "Notifiaction chat Created by Python"
if _name_ == "Notifiaction chat Created by Python":
    notifyMe("Ujjwal Saini","Ujjwal you are the python intermediate level programmer")
