#!/usr/bin/python3

from flask import Flask, url_for, request, jsonify, redirect
import hashlib
from random import randrange
# from YarpTp import YarpTp

app = Flask(__name__)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.one_request = True
# app.proto = None
app.base_url = '/api/v1'
app.token = None


def execute(direc, sp, mot, tm=0):
    if direc == 'forward':
        if sp is None:
            if tm == 0:
                if mot == 'left':
                    # app.proto.ForwardMotorL()
                    return jsonify(code=200, message='Moving ' + mot + ' motor - ' + direc)
                elif mot == 'right':
                    # app.proto.ForwardMotorR()
                    return jsonify(code=200, message='Moving ' + mot + ' motor - ' + direc)
                else:
                    # app.proto.Forward()
                    return jsonify(code=200, message='Moving both motors  - ' + direc)
            else:
                if mot == 'left':
                    # app.proto.ForwardMotorL(tm=tm)
                    return jsonify(code=200, message='Moving ' + mot + ' motor - ' + direc + ' during ' + str(tm) + ' seconds')
                elif mot == 'right':
                    # app.proto.ForwardMotorR(tm=tm)
                    return jsonify(code=200, message='Moving ' + mot + ' motor - ' + direc + ' during ' + str(tm) + ' seconds')
                else:
                    # app.proto.Forward(tm=tm)
                    return jsonify(code=200, message='Moving both motors  - ' + direc + ' during ' + str(tm) + ' seconds')
        else:
            if tm == 0:
                if mot == 'left':
                    # app.proto.ForwardMotorL(speed=sp)
                    return jsonify(code=200, message='Moving ' + mot + ' motor  - ' + direc + ' with speed ' + str(sp))
                elif mot == 'right':
                    # app.proto.ForwardMotorR(speed=sp)
                    return jsonify(code=200, message='Moving ' + mot + ' motor  - ' + direc + ' with speed ' + str(sp))
                else:
                    # app.proto.Forward(speed=sp)
                    return jsonify(code=200, message='Moving both motors  - ' + direc + ' with speed ' + str(sp))
            else:
                if mot == 'left':
                    # app.proto.ForwardMotorL(speed=sp, tm=tm)
                    return jsonify(code=200, message='Moving ' + mot + ' motor  - ' + direc + ' with speed ' + str(sp) + ' during ' + str(tm) + ' seconds')
                elif mot == 'right':
                    # app.proto.ForwardMotorR(speed=sp, tm=tm)
                    return jsonify(code=200, message='Moving ' + mot + ' motor  - ' + direc + ' with speed ' + str(sp) + ' during ' + str(tm) + ' seconds')
                else:
                    # app.proto.Forward(speed=sp, tm=tm)
                    print("IM IN EXECUTE")
                    return jsonify(code=200, message="Moving both motors  - " + direc + " with speed " + str(sp) + " during " + str(tm) + " seconds")
    elif direc == 'reverse':
        if sp is None:
            if tm == 0:
                if mot == 'left':
                    # app.proto.ReverseMotorL()
                    return jsonify(code=200, message='Moving ' + mot + ' motor - ' + direc)
                elif mot == 'right':
                    # app.proto.ReverseMotorR()
                    return jsonify(code=200, message='Moving ' + mot + ' motor - ' + direc)
                else:
                    # app.proto.Reverse()
                    return jsonify(code=200, message='Moving both motors  - ' + direc)
            else:
                if mot == 'left':
                    # app.proto.ReverseMotorL(tm=tm)
                    return jsonify(code=200, message='Moving ' + mot + ' motor - ' + direc + ' during ' + str(tm) + ' seconds')
                elif mot == 'right':
                    # app.proto.ReverseMotorR(tm=tm)
                    return jsonify(code=200, message='Moving ' + mot + ' motor - ' + direc + ' during ' + str(tm) + ' seconds')
                else:
                    # app.proto.Reverse(tm=tm)
                    return jsonify(code=200, message='Moving both motors  - ' + direc + ' during ' + str(tm) + ' seconds')
        else:
            if tm == 0:
                if mot == 'left':
                    # app.proto.ReverseMotorL(speed=sp)
                    return jsonify(code=200, message='Moving ' + mot + ' motor  - ' + direc + ' with speed ' + str(sp))
                elif mot == 'right':
                    # app.proto.ReverseMotorR(speed=sp)
                    return jsonify(code=200, message='Moving ' + mot + ' motor  - ' + direc + ' with speed ' + str(sp))
                else:
                    # app.proto.Reverse(speed=sp)
                    return jsonify(code=200, message='Moving both motors  - ' + direc + ' with speed ' + str(sp))
            else:
                if mot == 'left':
                    # app.proto.ReverseMotorL(speed=sp, tm=tm)
                    return jsonify(code=200, message='Moving ' + mot + ' motor  - ' + direc + ' with speed ' + str(sp) + ' during ' + str(tm) + ' seconds')
                elif mot == 'right':
                    # app.proto.ReverseMotorR(speed=sp, tm=tm)
                    return jsonify(code=200, message='Moving ' + mot + ' motor  - ' + direc + ' with speed ' + str(sp) + ' during ' + str(tm) + ' seconds')
                else:
                    # app.proto.Reverse(speed=sp, tm=tm)
                    return jsonify(code=200, message='Moving both motors  - ' + direc + ' with speed ' + str(sp) + ' during ' + str(tm) + ' seconds')
    else:
        return jsonify(code=400, message="SOY TU TORMENTO")


@app.route('/')
def index_first():
    return redirect(url_for('index'))


@app.route('/api/v1')
def index():
    tk = request.args.get('token')
    if app.token == None:
        return jsonify(code=200, message='Welcome to the API. Please go to the URL to Log in', url=url_for('login'))
    else:
        return jsonify(code=200, message='Welcome to the API. Go to the documentation for help')


@app.route(app.base_url + '/login')
def login():
    if app.one_request:
        # Primer usuario
        gen = hashlib.md5(str(randrange(2**15)).encode()).hexdigest()
        app.token = str(gen)
        app.one_request = False
        # app.proto = YarpTp()
    if not app.one_request:
        try:
            return jsonify(code=200, token=app.token)
        except KeyError:
            return jsonify(code=403, message='There is already a logged user')


@app.route(app.base_url + '/move/<string:motor>/<string:direction>')
@app.route(app.base_url + '/move/<string:motor>/<string:direction>/<float:time>')
@app.route(app.base_url + '/move/<string:motor>/<string:direction>/<int:speed>')
@app.route(app.base_url + '/move/<string:motor>/<string:direction>/<int:speed>/<float:time>')
def movement(motor, direction, speed=None, time=0):
    tk = request.args.get('token')
    if tk == app.token:
        print(app.token)
        print(motor, type(motor))
        print(direction, type(direction))
        print(time, type(time))
        print(speed, type(speed))
        if speed is not None:
            if not (0 <= speed <= 100):
                return jsonify(code=400, message='Wrong value of speed. Speed must be a float value between 0 and 100.')
            else:
                if motor == 'left' and direction == 'forward':
                    print(motor, direction)
                    return execute(mot=motor, direc=direction, sp=speed, tm=time)
                elif motor == 'left' and direction == 'reverse':
                    print(motor, direction)
                    return execute(mot=motor, direc=direction, sp=speed, tm=time)
                elif motor == 'right' and direction == 'forward':
                    print(motor, direction)
                    return execute(mot=motor, direc=direction, sp=speed, tm=time)
                elif motor == 'right' and direction == 'reverse':
                    print(motor, direction)
                    return execute(mot=motor, direc=direction, sp=speed, tm=time)
                elif motor == 'both' and direction == 'forward':
                    print(motor, direction)
                    return execute(mot=motor, direc=direction, sp=speed, tm=time)
                elif motor == 'both' and direction == 'reverse':
                    print(motor, direction)
                    return execute(mot=motor, direc=direction, sp=speed, tm=time)
                else:
                    if motor not in ['left', 'right', 'both'] and direction in ['forward', 'reverse']:
                        print("error1")
                        return jsonify(code=400, message='You are using a wrong motor instruction. Please, go to the documentation for help')
                    elif motor in ['left', 'right', 'both'] and direction not in ['forward', 'reverse']:
                        print("error2")
                        return jsonify(code=400, message='You are using a wrong direction instruction. Please, go to the documentation for help')
                    else:
                        print("error3")
                        return jsonify(code=404, message='This action does not exist. Please, go to the documentation for help')
        elif time != 0:
            if time <= 0:
                return jsonify(code=400, message='Wrong value of time. Time must be a integer value greater than 0.')
            else:
                if motor == 'left' and direction == 'forward':
                    print(motor, direction)
                    return execute(mot=motor, direc=direction, sp=speed, tm=time)
                elif motor == 'left' and direction == 'reverse':
                    print(motor, direction)
                    return execute(mot=motor, direc=direction, sp=speed, tm=time)
                elif motor == 'right' and direction == 'forward':
                    print(motor, direction)
                    return execute(mot=motor, direc=direction, sp=speed, tm=time)
                elif motor == 'right' and direction == 'reverse':
                    print(motor, direction)
                    return execute(mot=motor, direc=direction, sp=speed, tm=time)
                elif motor == 'both' and direction == 'forward':
                    print(motor, direction)
                    return execute(mot=motor, direc=direction, sp=speed, tm=time)
                elif motor == 'both' and direction == 'reverse':
                    print(motor, direction)
                    return execute(mot=motor, direc=direction, sp=speed, tm=time)
                else:
                    if motor not in ['left', 'right', 'both'] and direction in ['forward', 'reverse']:
                        print("error1")
                        return jsonify(code=400, message='You are using a wrong motor instruction. Please, go to the documentation for help')
                    elif motor in ['left', 'right', 'both'] and direction not in ['forward', 'reverse']:
                        print("error2")
                        return jsonify(code=400, message='You are using a wrong direction instruction. Please, go to the documentation for help')
                    else:
                        print("error3")
                        return jsonify(code=404, message='This action does not exist. Please, go to the documentation for help')
        else:
            print("ELEGIR")
            if motor == 'left' and direction == 'forward':
                print(motor, direction)
                return execute(mot=motor, direc=direction, sp=speed, tm=time)
            elif motor == 'left' and direction == 'reverse':
                print(motor, direction)
                return execute(mot=motor, direc=direction, sp=speed, tm=time)
            elif motor == 'right' and direction == 'forward':
                print(motor, direction)
                return execute(mot=motor, direc=direction, sp=speed, tm=time)
            elif motor == 'right' and direction == 'reverse':
                print(motor, direction)
                return execute(mot=motor, direc=direction, sp=speed, tm=time)
            elif motor == 'both' and direction == 'forward':
                print(motor, direction)
                return execute(mot=motor, direc=direction, sp=speed, tm=time)
            elif motor == 'both' and direction == 'reverse':
                print(motor, direction)
                return execute(mot=motor, direc=direction, sp=speed, tm=time)
            else:
                if motor not in ['left', 'right', 'both'] and direction in ['forward', 'reverse']:
                    print("error1")
                    return jsonify(code=400, message='You are using a wrong motor instruction. Please, go to the documentation for help')
                elif motor in ['left', 'right', 'both'] and direction not in ['forward', 'reverse']:
                    print("error2")
                    return jsonify(code=400, message='You are using a wrong direction instruction. Please, go to the documentation for help')
                else:
                    print("error3")
                    return jsonify(code=404, message='This action does not exist. Please, go to the documentation for help')
            print("El else donde se eligen")
        print("PASE")
    else:
        print("error no auth")
        return jsonify(code=401,
                       message='You are unauthorized to perform this action. Please, Log in in the URL',
                       url=url_for('login'))


@app.route(app.base_url + '/turn/<string:side>')
def turns(side):
    tk = request.args.get('token')
    if tk == app.token:
        if side == 'left':
            # app.proto.TurnLeft()
            return jsonify(code=200, message='Turning left the robot')
        elif side == 'right':
            # app.proto.TurnRight()
            return jsonify(code=200, message='Turning right the robot')
        else:
            return jsonify(code=400, message='You are using a wrong turn instruction. Please, go to the documentation for help')
    else:
        return jsonify(code=401,
                       message='You are unauthorized to perform this action. Please, Log in in the URL',
                       url=url_for('login'))


@app.route(app.base_url + '/move_step/<string:direction>')
def step(direction):
    tk = request.args.get('token')
    if tk == app.token:
        if direction == 'forward':
            # app.proto.ForwardStep()
            return jsonify(code=200, message='Moving one step in forward')
        elif direction == 'reverse':
            # app.proto.ReverseStep()
            return jsonify(code=200, message='Moving one step in reverse')
        else:
            return jsonify(code=400, message='You are using a wrong direction instruction. Please, go to the documentation for help')
    else:
        return jsonify(code=401,
                       message='You are unauthorized to perform this action. Please, Log in in the URL',
                       url=url_for('login'))


@app.route(app.base_url + '/stop')
def stop():
    tk = request.args.get('token')
    if tk == app.token:
        # app.proto.Stop()
        return jsonify(code=200, message='Stopping motors')
    else:
        return jsonify(code=401,
                       message='You are unauthorized to perform this action. Please, Log in in the URL',
                       url=url_for('login'))


@app.route(app.base_url + '/logout')
def logout():
    tk = request.args.get('token')
    if tk == app.token:
        # remove the username from the session if it's there
        app.one_request = True
        app.token = None
        # app.proto = None
        return jsonify(code=200, message='You have logged out')
    else:
        return jsonify(code=403, message='There is no logged user')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
