var interval = false
var interval_time = 60
var interval_step = 0

var maximum_brightness = 100
var minimum_brightness = 0
var minimum_difference = 10

function toggle_interval() {
  document.getElementById("start-marker").innerHTML = interval ? 'Start' : 'Stop'
  document.getElementById("start-button").classList.toggle("btn-success")
  document.getElementById("start-button").classList.toggle("btn-info")
  document.getElementById("interval-marker").innerHTML = interval_time

  interval_step = 0
  interval = !interval
}

function set_interval_time(val) {
  if (val > 4) {
    interval_time = parseInt(val)
    document.getElementById('interval-marker').innerHTML = val
  }
}

function set_maximum_brightness(val) {
  if (val > 0 && val < 101) {
    maximum_brightness = parseInt(val)
    document.getElementById('maximum-brightness-marker').innerHTML = val
  }
}

function set_minimum_brightness(val) {
  if (val > -1 && val < 101) {
    minimum_brightness = parseInt(val)
    document.getElementById('minimum-brightness-marker').innerHTML = val
  }
}

function set_minimum_difference(val) {
  if (val > -1 && val < 101) {
    minimum_difference = parseInt(val)
  }
}

setInterval(async () => {
  if (interval) {    
    if (interval_step >= interval_time) {
      pywebview.api.adjust_brightness(maximum_brightness, minimum_brightness, minimum_difference)
      interval_step = 0
    } else {
      interval_step++
    }
    document.getElementById("interval-marker").innerHTML = interval_time - interval_step
  } else {
    document.getElementById("interval-marker").innerHTML = interval_time
  }
}, 1000);