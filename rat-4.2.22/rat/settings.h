/*
 * FILE:    settings.h
 * PROGRAM: RAT
 * AUTHORS: Colin Perkins 
 *
 * Copyright (c) 1999-2001 University College London
 * All rights reserved.
 *
 * $Id: settings.h,v 1.8 2001/01/08 20:30:08 ucaccsp Exp $
 */

void settings_load_early(session_t *sp);
void settings_load_late(session_t *sp);
void settings_save(session_t *sp);

