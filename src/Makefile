
TARGET =  pcTutorial2 \
	kspTutorial34 \
	kspTutorial45 \
	kspTutorial50 

all : ${TARGET}

clean :
	rm -f ${TARGET}


pcTutorial2 : pcTutorial2.c
	g++  -o $@ $< -lpetsc

kspTutorial34 : kspTutorial34.c
	g++  -o $@ $< -lpetsc

kspTutorial45 : kspTutorial45.c 
	g++  -o $@ $< -lpetsc

kspTutorial50 : kspTutorial50.c 
	g++  -o $@ $< -lpetsc
