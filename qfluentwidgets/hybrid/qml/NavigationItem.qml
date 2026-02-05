import QtQuick 2.15

Item {
    id: control

    property string iconSymbol: ""
    property bool isCompact: false
    property bool isSelected: false
    property bool hovered: false
    property bool pressed: false
    property alias text: label.text

    signal clicked

    width: parent ? parent.width : 200
    height: 40

    children: [
        Rectangle {
            anchors.fill: parent
            color: control.pressed ? bridge.style.pressed : (control.hovered ? bridge.style.hover : "transparent")
            radius: 4
            children: [
                Rectangle {
                    visible: isSelected
                    width: 3
                    height: 16
                    radius: 1.5
                    color: bridge.style.accent
                    anchors.left: parent.left
                    anchors.leftMargin: 0
                    anchors.verticalCenter: parent.verticalCenter
                }
            ]
        },
        Item {
            id: iconBox
            width: 48
            height: parent.height
            anchors.left: parent.left
            anchors.verticalCenter: parent.verticalCenter
            children: [
                Image {
                    anchors.centerIn: parent
                    source: "image://FluentIcons/" + control.iconSymbol + "/" + bridge.theme + "/" + (isSelected ? (bridge.style.accent ? bridge.style.accent : bridge.style.text) : bridge.style.text)
                    width: 16
                    height: 16
                    sourceSize: Qt.size(16, 16)
                    visible: true
                }
            ]
        },
        Text {
            id: label
            visible: !isCompact
            font.family: "Segoe UI Variable Text"
            font.pixelSize: 14
            color: isSelected ? bridge.style.text : bridge.style.textSecondary
            anchors.left: iconBox.right
            anchors.verticalCenter: parent.verticalCenter
            leftPadding: 0
        },
        MouseArea {
            anchors.fill: parent
            hoverEnabled: true
            onEntered: control.hovered = true
            onExited: control.hovered = false
            onPressed: control.pressed = true
            onReleased: {
                control.pressed = false
                control.clicked()
            }
        }
    ]
}
