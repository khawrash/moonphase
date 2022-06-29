from flask import Flask, jsonify
from flask_cors import CORS
from skyfield.api import load
from skyfield.framelib import ecliptic_frame
from calc_time.calc_time import calc_time_return_dict

app = Flask(__name__)
CORS(app)

def calc_sun_moon_deg(dict_t):
    ts = load.timescale()
    t = ts.utc(dict_t['year'], dict_t['month'], dict_t['day'], dict_t['hour'], dict_t['minute'], dict_t['second'])
    eph = load('de421.bsp')
    sun, moon, earth = eph['sun'], eph['moon'], eph['earth']
    e = earth.at(t)
    _, slon, _ = e.observe(sun).apparent().frame_latlon(ecliptic_frame)
    _, mlon, _ = e.observe(moon).apparent().frame_latlon(ecliptic_frame)
    phase_deg = (mlon.degrees - slon.degrees) % 360.0
    #print('{0:.1f}'.format(phase_deg))
    return phase_deg

def calc_phase_from_deg(s_m_deg):
    if(s_m_deg >= 355 and s_m_deg < 5):
        return {"phaseNumber": 0, "phaseName": "new"}
    elif(s_m_deg >= 5 and s_m_deg < 89):
        return {"phaseNumber": 1, "phaseName": "waxing crescent"}
    elif(s_m_deg >= 89 and s_m_deg < 91):
        return {"phaseNumber": 2, "phaseName": "first quarter"}
    elif(s_m_deg >= 91 and s_m_deg < 179):
        return {"phaseNumber": 3, "phaseName": "waxing gibbous"}
    elif(s_m_deg >= 179 and s_m_deg < 181):
        return {"phaseNumber": 4, "phaseName": "full"}
    elif(s_m_deg >= 181 and s_m_deg < 269):
        return {"phaseNumber": 5, "phaseName": "waning gibbous"}
    elif(s_m_deg >= 269 and s_m_deg < 271):
        return {"phaseNumber": 6, "phaseName": "last quarter"}
    elif(s_m_deg >= 271 and s_m_deg < 355):
        return {"phaseNumber": 7, "phaseName": "waning crescent"}
    else:
        return {"phaseNumber": 404, "phaseName": "not found"}

@app.get("/phase")
def get_phase():
    dict_t = calc_time_return_dict('Asia/Jerusalem')
    phase_deg = calc_sun_moon_deg(dict_t)
    # phase = {"phaseNumber": 1, "phaseName": "first quarter"}
    return jsonify(calc_phase_from_deg(phase_deg))
