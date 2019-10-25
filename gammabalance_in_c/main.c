#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>	

int main (int argc, char** argv)
{
	//**enter judge(without guide
	if(argc != 3){
		printf("Wrong input!Exitting.\n");
                printf("Plese input \"./goBalance gammafile1.txt gammafile2.txt\".\n");
		return 0;
	}
	
	//**filename get
#if 0 
	//*typical input reading?
	int i = 0;
	char inputBuffer[50];
	for(i = 1;i < argc;i++){
		memcpy(inputBuffer,argv[i],50);
		printf("%s\n",inputBuffer);
	}	
#endif	
	errno = 0;
	char fileName1[50];
	char fileName2[50];	
	memcpy(fileName1,argv[1],50);
	memcpy(fileName2,argv[2],50);
	
	//**dateread
	FILE * pFile1;
	FILE * pFile2;
	
	pFile1 = fopen(fileName1,"r");
	if (pFile1 == NULL){
		printf("file1 open failed,%s\n",strerror(errno));
		return 0;
	}
	
	pFile2 = fopen(fileName2,"r");
	if (pFile2 == NULL){
		printf("file2 open failed,%s\n",strerror(errno));
		fclose(pFile1);
		return 0;
	}
	
	char* fileNameOut = "gammaBalance.txt";
	FILE * pFileOut;
	pFileOut = fopen(fileNameOut,"w");
	
	int counter = 0;
	int numbGot1 = 0;
	int numbGot2 = 0;
	int numbOut = 0;
	char charBuffer1[20];
	char charBuffer2[20];
	char charOut[20];
	char* readMark1;	
	char* readMark2;	
	while(1){			
		readMark1 = fgets(charBuffer1, 20 - 1, pFile1);
		readMark2 = fgets(charBuffer2, 20 - 1, pFile2);
		if (readMark1 == NULL || readMark2 == NULL) {
			if (!feof(pFile1)) {
				printf("fgetc() break in %s. count=%d \n",fileName1, counter);
			} else if(!feof(pFile2)) {			
				printf("fgetc() break in %s. count=%d \n",fileName2, counter);
			} else {
				printf("EOF reached \n");
			}
			break;
		} else {
			numbGot1 = atoi(charBuffer1);				
			printf("file1:%d",numbGot1);
			numbGot2 = atoi(charBuffer2);
			printf("file2:%d",numbGot2);
			
			//**balancing date
			numbOut = (numbGot1 + numbGot2) / 2	;
			//numbOut = numbGot1 + 63;	
			snprintf(charOut, 20, "%d\n", numbOut);			
			printf("file3:%s",charOut);
			
			//**datewrite
			if(fputs(charOut, pFileOut) == EOF){
				printf("fputs() break in %s. count=%d \n",fileNameOut, counter);
				break;
			}

			counter ++;
			continue; // ¼ÌÐø¸´ÖÆ
		}
		 

	}

	fclose(pFile1);
	fclose(pFile2);

	return 0;
}
