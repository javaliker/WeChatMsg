from PyQt5.QtGui import QIcon

from app.resources import resource_rc

var = resource_rc.qt_resource_name


class Icon:
    Default_avatar_path = ':/icons/icons/default_avatar.svg'
    Default_image_path = ':/icons/icons/404.png'
    MainWindow_Icon = QIcon(':/icons/icons/logo.svg')
    Default_avatar = QIcon(Default_avatar_path)
    Output = QIcon(':/icons/icons/output.svg')
    Back = QIcon(':/icons/icons/back.svg')
    ToDocx = QIcon(':/icons/icons/word.svg')
    ToCSV = QIcon(':/icons/icons/csv.svg')
    ToHTML = QIcon(':/icons/icons/html.svg')
    Chat_Icon = QIcon(':/icons/icons/chat.svg')
    Contact_Icon = QIcon(':/icons/icons/contact.svg')
    MyInfo_Icon = QIcon(':/icons/icons/myinfo.svg')
    Annual_Report_Icon = QIcon(':/icons/icons/annual_report.svg')
    Analysis_Icon = QIcon(':/icons/icons/analysis.svg')
    Emotion_Icon = QIcon(':/icons/icons/emotion.svg')
    Search_Icon = QIcon(':/icons/icons/search.svg')
