#!/usr/bin/env python3
import rospy
import tf
import sys
import select
import termios
import tty

# 초기 설정값
x, y, z = -0.1, 0.0, 0.0
yaw, pitch, roll = 1.570796, 0.0, 0.0

step_trans = 0.01  # 이동 단위 (1cm)
step_rot = 0.01    # 회전 단위 (약 0.5도)

msg = """
---------------------------
TF Fine Tuner
---------------------------
Move:
   q/w : X axis +/-
   e/r : Y axis +/-
   t/y : Z axis +/-

Rotate:
   a/s : Pitch +/-
   d/f : Yaw +/-
   g/h : Roll +/-

1/2 : Increase/Decrease Step Size
Space : Print current values
CTRL-C to quit
"""

def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)
    rospy.init_node('tf_fine_tuner')
    br = tf.TransformBroadcaster()
    rate = rospy.Rate(100) # 100hz

    print(msg)

    try:
        while not rospy.is_shutdown():
            key = getKey()
            
            # Translation
            if key == 'q': x += step_trans
            elif key == 'w': x -= step_trans
            elif key == 'e': y += step_trans
            elif key == 'r': y -= step_trans
            elif key == 't': z += step_trans
            elif key == 'y': z -= step_trans
            
            # 회전 Rotation
            elif key == 'a': yaw += step_rot
            elif key == 's': yaw -= step_rot
            elif key == 'd': pitch += step_rot
            elif key == 'f': pitch -= step_rot
            elif key == 'g': roll += step_rot
            elif key == 'h': roll -= step_rot

            # 스텝 조절
            elif key == '1': 
                step_trans *= 0.5
                step_rot *= 0.5
                print(f"Step Scale: Trans={step_trans:.4f}, Rot={step_rot:.4f}")
            elif key == '2': 
                step_trans *= 2.0
                step_rot *= 2.0
                print(f"Step Scale: Trans={step_trans:.4f}, Rot={step_rot:.4f}")
                
            elif key == ' ':
                print(f"Current: {x:.4f} {y:.4f} {z:.4f} {yaw:.4f} {pitch:.4f} {roll:.4f}")
            elif key == '\x03': # CTRL-C
                break

            br.sendTransform((x, y, z),
                             tf.transformations.quaternion_from_euler(roll, pitch, yaw),
                             rospy.Time.now(),
                             "cam_2_link",  # child
                             "base_link")  # parent
            rate.sleep()

    except Exception as e:
        print(e)

    finally:
        print(f"\nFINAL VALUES: {x:.4f} {y:.4f} {z:.4f} {yaw:.4f} {pitch:.4f} {roll:.4f}")
        print("Copy these values to your launch file or static_transform_publisher.")
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
