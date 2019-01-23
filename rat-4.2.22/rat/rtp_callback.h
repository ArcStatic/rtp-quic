/*
 * FILE:    rtp_callback.h
 * PROGRAM: RAT
 * AUTHOR:  Colin Perkins / Orion Hodson
 *
 * Copyright (c) 1999-2001 University College London
 * All rights reserved.
 *
 * $Id: rtp_callback.h,v 1.8 2001/03/28 14:32:00 ucacoxh Exp $
 */

#ifndef __RTP_CALLBACK_H__
#define __RTP_CALLBACK_H__

struct s_session;

void rtp_callback_init (struct rtp *s, struct s_session *sp);
void rtp_callback_proc (struct rtp *s, rtp_event *e);
void rtp_callback_exit (struct rtp *s);

#endif /* __RTP_CALLBACK_H__ */
