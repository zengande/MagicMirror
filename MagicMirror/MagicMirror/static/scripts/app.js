const weekday = ["周日", "周一", "周二", "周三", "周四", "周五", "周六"];

const app = new Vue({
    el: '#app',
    data: {
        hours: "00",
        minutes: "00",
        seconds: "00",
        date: '',
        holidays: [],
        lunarDate: '',
        indoor_env: {
            temperature: "N/A",
            humidity: "N/A"
        },
        outdoor_env: {
            cond_code: "999",
            temperature: "N/A"
        }
    },
    created: function () {
        const that = this;
        const namespace = "/monitor";
        var socket = io.connect('http://' + document.domain + ':' + location.port + namespace);

        socket.on('response_ht', (data) => {
            const { temperature, humidity } = data;
            that.indoor_env = {
                temperature: temperature || "N/A",
                humidity: humidity || "N/A"
            };
        });
    }
});

updateTime();
setInterval(updateTime, 1000);



function updateTime() {
    var now = new Date();
    app.hours = pad(now.getHours(), 2);
    app.minutes = pad(now.getMinutes(), 2);
    app.seconds = pad(now.getSeconds(), 2);

    var year = now.getFullYear();
    var month = now.getMonth() + 1;
    var day = now.getDate();
    var lunarDate = sloarToLunar(year, month, day);
    app.lunarDate = `${lunarDate.lunarYear}年 ${lunarDate.lunarMonth}月${lunarDate.lunarDay}`;
    app.date = `${pad(month, 2)}月${pad(day, 2)}日 ${weekday[now.getDay()]}`;
    var jq = getJQ(year, month, day);
    if (jq !== '') {
        app.holidays = [jq];
    }
}

function pad(n, width, z) {
    z = z || '0';
    n = n + '';
    return n.length >= width ? n : new Array(width - n.length + 1).join(z) + n;
}
