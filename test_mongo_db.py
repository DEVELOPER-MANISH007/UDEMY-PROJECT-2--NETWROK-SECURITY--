from pymongo import MongoClient
import socket
MONGODB_URI="mongodb://manish8755026341_db_user:VqtBJEoxx6JZ3JMT@ac-ees2chm-shard-00-00.vxjahgj.mongodb.net:27017,ac-ees2chm-shard-00-01.vxjahgj.mongodb.net:27017,ac-ees2chm-shard-00-02.vxjahgj.mongodb.net:27017/?ssl=true&replicaSet=atlas-11sej7-shard-0&authSource=admin&appName=Cluster0"
# Set longer DNS timeout
socket.setdefaulttimeout(60)


try:
    client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=30000, connectTimeoutMS=30000)
    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    print(f"Error: {e}")
    print("\n⚠️ Possible causes:")
    print("1. MongoDB Atlas cluster IP whitelist - add your IP address")
    print("2. Network/Firewall blocking DNS or MongoDB ports")
    print("3. Invalid credentials")
    print("4. MongoDB cluster offline or not responding")