# Github for Glog project M2 Bioinfo Bordeaux

## First steps using the app :
- If you don't have python3 :
```bash
sudo apt-get install python3
```

- Install Django :

```bash
pip3 install Django==2.1.5 
```

- If you use BioPython , install Biopython : 

```bash
pip3 install biopython
```

- Install ncbi-blast+ in order to launch local blast:

```bash
sudo apt install ncbi-blast+
```

Then clone the project with this command :

```bash
git clone https://github.com/s3bc40/gLogProject.git
```

To run the server :

```bash
cd server
python3 manage.py runserver
```

You should be able to see the webApp at the adress : http://127.0.0.1:8000/

> NOTE : create a branch for your work ! Don't make changes in the master django server.

If you want to update the django server version in the master, from your branch :

```bash
git checkout master
git checkout YOUR_BRANCH -- server
```
## The source code is in the server repository 
