#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#define BUFLEN 1024


//argv[1] = message to send to server
int main(int argc, char **argv){
    
    int client_fd;
    int msg_len;
    char *recvbuf;
    struct sockaddr_in addr_info;
    struct sockaddr_in server_info;
    
    recvbuf = (char*) malloc(BUFLEN);
 
    client_fd = socket(AF_INET, SOCK_DGRAM, 0);
    
    addr_info.sin_family = AF_INET;
    addr_info.sin_port = htons(5005);
    inet_aton("127.0.0.1", &addr_info.sin_addr);
    
    server_info.sin_family = AF_INET;
    server_info.sin_port = htons(5004);
    inet_aton("127.0.0.1", &server_info.sin_addr);
    
    bind(client_fd, (struct sockaddr *)&addr_info, sizeof(addr_info));
    
    sendto(client_fd, argv[1], strlen(argv[1]), 0, (struct sockaddr *)&server_info, sizeof(server_info));
    
    msg_len = recvfrom(client_fd, recvbuf, BUFLEN, 0, (struct sockaddr *)&server_info, (socklen_t*)sizeof(&server_info));
    recvbuf[msg_len] = '\0';
    
    printf("Message received: %s\n", recvbuf);
    
    free(recvbuf);
    
}
