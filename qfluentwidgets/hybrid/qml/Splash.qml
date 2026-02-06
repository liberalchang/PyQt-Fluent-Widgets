import QtQuick 2.15
import FluentUI 1.0

Rectangle {
    id: root
    width: 640
    height: 420
    color: isDark ? "#0f172a" : "#f0f2f5"
    radius: 12

    property var bridgeObj: (typeof bridge !== "undefined") ? bridge : null
    property bool isDark: bridgeObj ? bridgeObj.isDark : false
    property string titleText: bridgeObj ? bridgeObj.titleText : "应用启动中"
    property string descriptionText: bridgeObj ? bridgeObj.descriptionText : "正在加载，请稍候……"
    property string iconPath: bridgeObj ? bridgeObj.iconPath : ""
    property string iconColor: bridgeObj ? bridgeObj.iconColor : ""

    property color contentColor: isDark ? "#ffffff" : "#333333"
    property color particleColor: isDark ? Qt.rgba(1,1,1,0.5) : Qt.rgba(0,0,0,0.5)

    property int particleCount: 90
    property var particles: []

    Behavior on color { ColorAnimation { duration: 500 } }

    Component.onCompleted: {
        particles = []
        for (var i = 0; i < particleCount; ++i) {
            particles.push({
                x: Math.random() * width,
                y: Math.random() * height,
                vx: (Math.random() - 0.5) * 0.8,
                vy: (Math.random() - 0.5) * 0.8,
                r: 1.2 + Math.random() * 1.0
            })
        }
        canvas.requestPaint()
        animTimer.start()
    }

    Canvas {
        id: canvas
        anchors.fill: parent
        antialiasing: true
        renderTarget: Canvas.Image

        onPaint: {
            var ctx = getContext("2d")
            ctx.clearRect(0, 0, width, height)

            ctx.fillStyle = particleColor
            for (var i = 0; i < particles.length; ++i) {
                var p = particles[i]
                ctx.beginPath()
                ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2)
                ctx.fill()
            }

            var threshold = 140
            for (var a = 0; a < particles.length; ++a) {
                for (var b = a + 1; b < particles.length; ++b) {
                    var pa = particles[a], pb = particles[b]
                    var dx = pa.x - pb.x, dy = pa.y - pb.y
                    var dist = Math.sqrt(dx*dx + dy*dy)
                    if (dist < threshold) {
                        var alpha = 1.0 - dist / threshold
                        ctx.strokeStyle = Qt.rgba(particleColor.r, particleColor.g, particleColor.b, alpha)
                        ctx.beginPath()
                        ctx.moveTo(pa.x, pa.y)
                        ctx.lineTo(pb.x, pb.y)
                        ctx.stroke()
                    }
                }
            }
        }
    }

    Timer {
        id: animTimer
        interval: 16
        repeat: true
        running: false
        onTriggered: {
            for (var i = 0; i < particles.length; ++i) {
                var p = particles[i]
                p.x += p.vx
                p.y += p.vy
                if (p.x < 0 || p.x > root.width) p.vx = -p.vx
                if (p.y < 0 || p.y > root.height) p.vy = -p.vy
            }
            canvas.requestPaint()
        }
    }

    Column {
        anchors.centerIn: parent
        spacing: 12

        SvgIcon {
            width: 72
            height: 72
            anchors.horizontalCenter: parent.horizontalCenter
            source: iconPath
            color: iconColor ? iconColor : contentColor
        }

        Text {
            anchors.horizontalCenter: parent.horizontalCenter
            text: titleText
            color: contentColor
            font.family: "Segoe UI Variable Text"
            font.pixelSize: 18
        }

        Text {
            anchors.horizontalCenter: parent.horizontalCenter
            text: descriptionText
            color: isDark ? "#DDFFFFFF" : "#99000000"
            font.family: "Segoe UI Variable Text"
            font.pixelSize: 13
        }
    }
}
