import paramiko
import yaml

def getTargetFiles():
    with open("target.yaml") as f:
        target = yaml.load(f, Loader=yaml.FullLoader)
        remotePrefix = f"{target['remote']}/{target['project']}"
        localPrefix = target["local"].replace('\\', '/')
        localFiles = []
        remoteFiles = []
        for file in target["files"]:
            file = file.replace('\\', '/')
            localFiles.append(f"{localPrefix}/{file}")
            remoteFiles.append(f"{remotePrefix}/{file}")

        return localFiles, remoteFiles


def getTargetDirectory():
    with open("target.yaml") as f:
        target = yaml.load(f, Loader=yaml.FullLoader)
        remote = target["remote"]
        project = target["project"]
        remotePrefix = f"{remote}/{project}"
        localPrefix = target["local"].replace('\\', '/')
        localFiles = []
        for file in target["files"]:
            localFiles.append(file.replace('\\', '/'))

        print(localPrefix)
        print(remotePrefix)

        dirSet = set()
        for file in localFiles:
            remoteFile = f"{remotePrefix}/{file}"
            tmp = remoteFile.split('/')

            dirPath = ''
            for folder in tmp[0:len(tmp) - 1]:
                if folder == '':
                    continue
                dirPath = f"{dirPath}/{folder}"
                dirSet.update([dirPath])
            # print(dirPath)

        dirSet = list(dirSet)
        dirSet.sort()
        return dirSet


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("3.36.66.126", username="ec2-user", key_filename="D:/ZHKim/measset-ami.pem")
stdin, stdout, stderr = ssh.exec_command("ls")
print(stdout.readlines())

sftp = ssh.open_sftp()
targetDirList = getTargetDirectory()
for path in targetDirList:
    try:
        sftp.stat(path)
    except:
        sftp.mkdir(path)
        print(f"Created '{path}'")

localFiles, remoteFiles = getTargetFiles()
for i in range(0, len(localFiles)):
    local, remote = localFiles[i], remoteFiles[i]
    # sftp.put(local, remote)
    sftp.get(remote, local)
# sftp.get("/home/ec2-user/uploads/files/hambok.jpg", "D:/tmp/hambok2.jpg")
sftp.close()
ssh.close()