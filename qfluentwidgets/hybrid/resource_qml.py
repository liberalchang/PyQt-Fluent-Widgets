# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.9.3
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x00\xaf\
i\
mport QtQuick\x0a\x0aR\
ectangle {\x0a    c\
olor: \x22red\x22\x0a    \
width: 100\x0a    h\
eight: 100\x0a    \x0a\
    MouseArea {\x0a\
        anchors.\
fill: parent\x0a   \
     onClicked: \
console.log(\x22Cli\
cked\x22)\x0a    }\x0a}\
\x00\x00\x08\xba\
i\
mport QtQuick\x0aim\
port QtQuick.Con\
trols.Basic\x0aimpo\
rt QtQuick.Layou\
ts\x0aimport \x22.\x22\x0a\x0aR\
ectangle {\x0a    i\
d: root\x0a    \x0a   \
 property string\
 currentTheme: \x22\
Light\x22\x0a    // th\
eme property is \
no longer needed\
 as we use globa\
l Style\x0a    prop\
erty bool isComp\
act: width < 100\
 \x0a\x0a    color: br\
idge.style.backg\
round\x0a    \x0a    C\
olumnLayout {\x0a  \
      anchors.fi\
ll: parent\x0a     \
   anchors.margi\
ns: isCompact ? \
0 : 4\x0a        sp\
acing: 4\x0a       \
 \x0a        // Hea\
der (Hamburger)\x0a\
        Item {\x0a \
           Layou\
t.fillWidth: tru\
e\x0a            La\
yout.preferredHe\
ight: 36\x0a       \
     \x0a          \
  Button {\x0a     \
           id: h\
amburger\x0a       \
         width: \
40\x0a             \
   height: 36\x0a  \
              an\
chors.left: pare\
nt.left\x0a        \
        anchors.\
verticalCenter: \
parent.verticalC\
enter\x0a          \
      \x0a         \
       backgroun\
d: Rectangle {\x0a \
                \
   color: parent\
.pressed ? bridg\
e.style.pressed \
: (parent.hovere\
d ? bridge.style\
.hover : \x22transp\
arent\x22)\x0a        \
            radi\
us: 4\x0a          \
      }\x0a        \
        \x0a       \
         content\
Item: Item {\x0a   \
                \
 anchors.centerI\
n: parent\x0a      \
              wi\
dth: 16\x0a        \
            heig\
ht: 16\x0a         \
           \x0a    \
                \
Image {\x0a        \
                \
anchors.centerIn\
: parent\x0a       \
                \
 source: \x22image:\
//FluentIcons/Me\
nu/\x22 + bridge.th\
eme + \x22/\x22 + (bri\
dge.theme === \x22D\
ark\x22 ? \x22#FFFFFF\x22\
 : \x22#000000\x22)\x0a  \
                \
      width: 16\x0a\
                \
        height: \
16\x0a             \
           sourc\
eSize: Qt.size(1\
6, 16)\x0a         \
           }\x0a   \
             }\x0a \
               \x0a\
                \
onClicked: {\x0a   \
                \
 bridge.menuClic\
ked(\x22toggle_side\
bar\x22)\x0a          \
      }\x0a        \
    }\x0a        }\x0a\
        \x0a       \
 // Navigation L\
ist\x0a        List\
View {\x0a         \
   id: navList\x0a \
           Layou\
t.fillWidth: tru\
e\x0a            La\
yout.fillHeight:\
 true\x0a          \
  clip: true\x0a   \
         model: \
navItems\x0a       \
     spacing: 2\x0a\
            \x0a   \
         delegat\
e: NavigationIte\
m {\x0a            \
    text: modelD\
ata.text\x0a       \
         iconSym\
bol: modelData.i\
con\x0a            \
    isCompact: r\
oot.isCompact\x0a  \
              \x0a \
               o\
nClicked: {\x0a    \
                \
bridge.menuClick\
ed(modelData.rou\
teKey)\x0a         \
       }\x0a       \
     }\x0a        }\
\x0a    }\x0a}\x0a\
\x00\x00\x06\xc6\
i\
mport QtQuick\x0aim\
port QtQuick.Con\
trols.Basic\x0aimpo\
rt QtQuick.Layou\
ts\x0aimport \x22.\x22\x0a\x0aI\
temDelegate {\x0a  \
  id: control\x0a  \
  \x0a    property \
string iconSymbo\
l: \x22\x22\x0a    proper\
ty bool isCompac\
t: false\x0a    pro\
perty bool isSel\
ected: false\x0a   \
 \x0a    width: par\
ent.width\x0a    he\
ight: 40\x0a    \x0a  \
  background: Re\
ctangle {\x0a      \
  color: control\
.pressed ? bridg\
e.style.pressed \
: (control.hover\
ed ? bridge.styl\
e.hover : \x22trans\
parent\x22)\x0a       \
 radius: 4\x0a     \
   \x0a        // S\
election Indicat\
or (Active Bar)\x0a\
        Rectangl\
e {\x0a            \
visible: isSelec\
ted\x0a            \
width: 3\x0a       \
     height: 16\x0a\
            radi\
us: 1.5\x0a        \
    color: bridg\
e.style.accent\x0a \
           ancho\
rs.left: parent.\
left\x0a           \
 anchors.leftMar\
gin: 0 \x0a        \
    anchors.vert\
icalCenter: pare\
nt.verticalCente\
r\x0a        }\x0a    \
}\x0a\x0a    contentIt\
em: Row {\x0a      \
  spacing: 0\x0a   \
     \x0a        //\
 Icon Area\x0a     \
   Item {\x0a      \
      width: 48 \
// Standard nav \
width\x0a          \
  height: parent\
.height\x0a        \
    \x0a           \
 Image {\x0a       \
         id: ico\
nImg\x0a           \
     anchors.cen\
terIn: parent\x0a  \
              so\
urce: \x22image://F\
luentIcons/\x22 + c\
ontrol.iconSymbo\
l + \x22/\x22 + bridge\
.theme + \x22/\x22 + (\
isSelected ? (br\
idge.style.accen\
t || \x22#009FAA\x22) \
: (bridge.theme \
=== \x22Dark\x22 ? \x22#F\
FFFFF\x22 : \x22#00000\
0\x22))\x0a           \
     width: 16\x0a \
               h\
eight: 16\x0a      \
          source\
Size: Qt.size(16\
, 16)\x0a          \
      visible: t\
rue\x0a            \
}\x0a        }\x0a    \
    \x0a        // \
Text Area\x0a      \
  Text {\x0a       \
     visible: !i\
sCompact\x0a       \
     text: contr\
ol.text\x0a        \
    font.family:\
 \x22Segoe UI Varia\
ble Text\x22\x0a      \
      font.pixel\
Size: 14\x0a       \
     color: brid\
ge.style.text\x0a  \
          anchor\
s.verticalCenter\
: parent.vertica\
lCenter\x0a        \
    leftPadding:\
 0\x0a        }\x0a   \
 }\x0a}\x0a\
\x00\x00\x01J\
Q\
Object[theme=\x22Li\
ght\x22] {\x0a    qpro\
perty-background\
: #f3f3f3;\x0a    q\
property-surface\
: #ffffff;\x0a    q\
property-surface\
Highlight: #e5e5\
e5;\x0a    qpropert\
y-text: #000000;\
\x0a    qproperty-t\
extSecondary: #6\
66666;\x0a    qprop\
erty-hover: #100\
00000;\x0a    qprop\
erty-pressed: #0\
8000000;\x0a    qpr\
operty-border: #\
e5e5e5;\x0a    qpro\
perty-accent: #0\
09faa;\x0a}\x0a\
\x00\x00\x01I\
Q\
Object[theme=\x22Da\
rk\x22] {\x0a    qprop\
erty-background:\
 #202020;\x0a    qp\
roperty-surface:\
 #2d2d2d;\x0a    qp\
roperty-surfaceH\
ighlight: #3b3b3\
b;\x0a    qproperty\
-text: #ffffff;\x0a\
    qproperty-te\
xtSecondary: #cc\
cccc;\x0a    qprope\
rty-hover: #10ff\
ffff;\x0a    qprope\
rty-pressed: #08\
ffffff;\x0a    qpro\
perty-border: #3\
b3b3b;\x0a    qprop\
erty-accent: #76\
b9ed;\x0a}\x0a\
"

qt_resource_name = b"\
\x00\x03\
\x00\x00x\xa3\
\x00q\
\x00s\x00s\
\x00\x03\
\x00\x00x<\
\x00q\
\x00m\x00l\
\x00\x0c\
\x03\xe45\x1c\
\x00T\
\x00i\x00t\x00l\x00e\x00B\x00a\x00r\x00.\x00q\x00m\x00l\
\x00\x12\
\x0b\xc0P|\
\x00S\
\x00i\x00d\x00e\x00N\x00a\x00v\x00i\x00g\x00a\x00t\x00i\x00o\x00n\x00.\x00q\x00m\
\x00l\
\x00\x12\
\x0e?\xb1|\
\x00N\
\x00a\x00v\x00i\x00g\x00a\x00t\x00i\x00o\x00n\x00I\x00t\x00e\x00m\x00.\x00q\x00m\
\x00l\
\x00\x04\
\x00\x06\xa8\x8b\
\x00d\
\x00a\x00r\x00k\
\x00\x05\
\x00r\xfd\xf4\
\x00l\
\x00i\x00g\x00h\x00t\
\x00\x09\
\x0c8\xadc\
\x00t\
\x00h\x00e\x00m\x00e\x00.\x00q\x00s\x00s\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x0c\x00\x02\x00\x00\x00\x03\x00\x00\x00\x08\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x04\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x8a\x00\x02\x00\x00\x00\x01\x00\x00\x00\x07\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x98\x00\x02\x00\x00\x00\x01\x00\x00\x00\x06\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\xa8\x00\x00\x00\x00\x00\x01\x00\x00\x10;\
\x00\x00\x01\x9c+\xeb\x02\x94\
\x00\x00\x00\xa8\x00\x00\x00\x00\x00\x01\x00\x00\x11\x89\
\x00\x00\x01\x9c+\xeb\x06\xf1\
\x00\x00\x00\x18\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x9c- \xe3\xe8\
\x00\x00\x006\x00\x00\x00\x00\x00\x01\x00\x00\x00\xb3\
\x00\x00\x01\x9c- \x16\x08\
\x00\x00\x00`\x00\x00\x00\x00\x00\x01\x00\x00\x09q\
\x00\x00\x01\x9c-\x1f\xc4\x7f\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
