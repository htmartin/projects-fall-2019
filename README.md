# projects-fall-2019

### Python

###for just python shell

docker run -it --rm -v`pwd`:/tmartin midsw205/base:latest


at container prompt,

python


## run jupyter in container

source ~/venv/bin/activate

-run this in home or wherever
docker run -it --rm -p 8888:8888 -v`pwd`:/tmartin midsw205/base:latest

-in container
cd /tmartin
jupyter notebook --no-browser --port 8888 --ip=0.0.0.0 --allow-root 


-Then take token and put in once run: 

-MIT edx

- https://courses.edx.org/courses/course-v1:MITx+6.00.1x+2T2019a/courseware/fc8f42302c644118adfcfa720f9f403e/35f82f6c3ecb4e9e913dc279a9b73a9f/6?activate_block_id=block-v1%3AMITx%2B6.00.1x%2B2T2019a%2Btype%40problem%2Bblock%40052c7be3bb5e43c195f678dab070776d

-datacamp



### typing


### Dis ed research