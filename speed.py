import speedtest
import math
def speed():
    st = speedtest.Speedtest()



    def bytes_to_Mb(size_bytes):
        i = int(math.floor(math.log(size_bytes,1024)))
        power = math.pow(1024,i)
        size = round(size_bytes/power,2)
        return size

    speed_MB = bytes_to_Mb(st.download())/8
    return speed_MB
