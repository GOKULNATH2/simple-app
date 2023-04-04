import subprocess
import os
def get_changed_folders():
    cmd = "git log -1 --pretty=format: d5bb98e705f9476178a1496942eddcb1dd9caf3d"
    res = execute_command(cmd.split())
    print("res:",res)


def execute_command(cmd, preexec_fn=False):
    try:
        response = {}
        p = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE,preexec_fn= os.setsid if preexec_fn else None)
        out,err = p.communicate()
        response["out"] = out.decode("utf-8") if out.decode("utf-8") else ""
        if err.decode("utf-8"):
            response["error"] = err.decode('utf-8')
        return response
    except Exception as e:
        print('error')
        raise e
    
if __name__ == '__main__':
    get_changed_folders()
