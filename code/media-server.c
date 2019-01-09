#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#define BUFLEN 1024


//argv[1] = message to send to client
int main(int argc, char **argv){
    
    int server_fd;
    int msg_len;
    int client_len;
    char *recvbuf;
    struct sockaddr_in addr_info;
    struct sockaddr_in client_info;
    
    recvbuf = (char*) malloc(BUFLEN);
    
    server_fd = socket(AF_INET, SOCK_DGRAM, 0);
    
    addr_info.sin_family = AF_INET;
    addr_info.sin_port = htons(5004);
    inet_aton("127.0.0.1", &addr_info.sin_addr);
    
    client_len = sizeof(client_info);
    
    bind(server_fd, (struct sockaddr *)&addr_info, sizeof(addr_info));

    msg_len = recvfrom(server_fd, recvbuf, BUFLEN, 0, (struct sockaddr *)&client_info, (socklen_t*)&client_len);
    recvbuf[msg_len] = '\0';
    
    printf("Message received: %s\n", recvbuf);

    sendto(server_fd, argv[1], strlen(argv[1]), 0, (struct sockaddr *)&client_info, client_len);
    
    printf("Message sent to %s, %d\n", inet_ntoa(client_info.sin_addr), ntohs(client_info.sin_port));
    
    free(recvbuf);
    
}
