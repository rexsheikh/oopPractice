from alarm_clock import AlarmClock

rexs_alarm_clock = AlarmClock()

print(rexs_alarm_clock.alarm_time)
rexs_alarm_clock.change_time('1300')
rexs_alarm_clock.alarm_toggle(False)
print(rexs_alarm_clock.alarm_on)