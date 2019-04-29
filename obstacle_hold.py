import rospy
from math import sqrt
from std_msgs.msg import String
from sensor_msgs import point_cloud2
from sensor_msgs.msg import PointCloud2 
from dronekit import connect
import dronekit

v = connect("/dev/ttyACM2")

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/ti_mmwave/radar_scan_pcl", PointCloud2, callback_pointcloud)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

THR_DIST = 5

def callback_pointcloud(data):

    assert isinstance(data, PointCloud2)

    gen = point_cloud2.read_points(data)

    point_cnt = 0
    in_vicinity = 0

    for p in gen:
        point_cnt += 1
        if(sqrt(p[0]**2+p[1]**2) < 2):

            in_vicinity += p[3]
	#print p  # type depends on your data type, first three entries are probably x,y,z_name__ == '__main__':

    #print point_cnt
    if(in_vicinity > 300):
        print "STOP"
        v.mode = dronekit.VehicleMode("HOLD")
    else:
        print "FLY"

if __name__ == '__main__':
    listener()

