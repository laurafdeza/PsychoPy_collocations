#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.2),
    on Thu Mar 14 13:24:40 2019
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.0.2'
expName = 'expressions_knowledge'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/lfa/Desktop/colls_lex_task 2/expressions_knowledge_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0,
    allowGUI=True, allowStencil=False,
    monitor='testMonitor', color='#000000', colorSpace='hex',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Intro"
IntroClock = core.Clock()
Welcome = visual.TextStim(win=win, name='Welcome',
    text='Bienvenido.\n\nVas a completar una sesión de tres tests.\nEn total tardarás 10 minutos máximo.\n\nPulsa la barra espaciadora (space) cuando estés listo/a para empezar.',
    font='Calibri',
    pos=(0, 0), height=0.1, wrapWidth=1000, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Instructions_comprehension"
Instructions_comprehensionClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Test 1\n\nEscoge pinchando con el ratón la opción que corresponde con la expresión en mayúscula.\n\nPulsa la barra espaciadora (space) cuando estés listo/a para empezar.',
    font='Calibri',
    pos=(0, 0), height=0.1, wrapWidth=1000, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "definition"
definitionClock = core.Clock()
sentences = visual.TextStim(win=win, name='sentences',
    text='default text',
    font='Arial',
    pos=(0, .5), height=0.1, wrapWidth=1000, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
resp_A = visual.TextStim(win=win, name='resp_A',
    text='default text',
    font='Arial',
    pos=(0, .25), height=0.1, wrapWidth=1000, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
resp_B = visual.TextStim(win=win, name='resp_B',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1000, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
resp_C = visual.TextStim(win=win, name='resp_C',
    text='default text',
    font='Arial',
    pos=(0, -.25), height=0.1, wrapWidth=1000, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
resp_D = visual.TextStim(win=win, name='resp_D',
    text='default text',
    font='Arial',
    pos=(0, -.5), height=0.1, wrapWidth=1000, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "fin_1"
fin_1Clock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text='Fin del primer test.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1000, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Instruction_English"
Instruction_EnglishClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Test 2\n\nEscoge pinchando con el ratón la definición de cada expresión\n\nPulsa la barra espaciadora cuando estés listo/a para empezar.',
    font='Calibri',
    pos=(0, 0), height=0.1, wrapWidth=1000, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "expression"
expressionClock = core.Clock()
EN_exp = visual.TextStim(win=win, name='EN_exp',
    text='default text',
    font='Calibri',
    pos=[0,0], height=0.1, wrapWidth=1000, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
ans_A = visual.TextStim(win=win, name='ans_A',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=1000, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
reg_A = visual.Rect(
    win=win, name='reg_A',
    width=(1.0, 1.0)[0], height=(1.0, 1.0)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-2.0, interpolate=True)
ans_B = visual.TextStim(win=win, name='ans_B',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=1000, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
reg_B = visual.Rect(
    win=win, name='reg_B',
    width=(1.0, 1.0)[0], height=(1.0, 1.0)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-4.0, interpolate=True)
ans_C = visual.TextStim(win=win, name='ans_C',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=1000, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
reg_C = visual.Rect(
    win=win, name='reg_C',
    width=(1.0, 1.0)[0], height=(1.0, 1.0)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-6.0, interpolate=True)
ans_D = visual.TextStim(win=win, name='ans_D',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=1000, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
reg_D = visual.Rect(
    win=win, name='reg_D',
    width=(1.0, 1.0)[0], height=(1.0, 1.0)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-8.0, interpolate=True)
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()


# Initialize components for Routine "fin_2"
fin_2Clock = core.Clock()
text_9 = visual.TextStim(win=win, name='text_9',
    text='Fin del segundo test.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1000, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Instruction_knowledge"
Instruction_knowledgeClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Test 3\n\nEscoge pinchando con el ratón la traducción en inglés de cada expresión que escuchas en español. Hay más expresiones en inglés que en español.\n\nPrimero vas a ver las expresiones en inglés, cuando estés listo, pulsa la barra espaciadora.\n\nPulsa la barra espaciadora cuando estés listo/a para empezar.',
    font='Calibri',
    pos=(0, 0), height=0.1, wrapWidth=1000, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "memory"
memoryClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=1000, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1000, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_6 = visual.TextStim(win=win, name='text_6',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=1000, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_7 = visual.TextStim(win=win, name='text_7',
    text="Pulsa 'space' cuando estés listo/a para empezar",
    font='Arial',
    pos=(0, -.9), height=0.04, wrapWidth=1000, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "audio"
audioClock = core.Clock()
rpA = visual.TextStim(win=win, name='rpA',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.08, wrapWidth=1000, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
rpB = visual.TextStim(win=win, name='rpB',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.08, wrapWidth=1000, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
rpC = visual.TextStim(win=win, name='rpC',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.08, wrapWidth=1000, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
rpD = visual.TextStim(win=win, name='rpD',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.08, wrapWidth=1000, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
rpE = visual.TextStim(win=win, name='rpE',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.08, wrapWidth=1000, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
rpF = visual.TextStim(win=win, name='rpF',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.08, wrapWidth=1000, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
rpG = visual.TextStim(win=win, name='rpG',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.08, wrapWidth=1000, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
rpH = visual.TextStim(win=win, name='rpH',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.08, wrapWidth=1000, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
rpJ = visual.TextStim(win=win, name='rpJ',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.08, wrapWidth=1000, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
rpK = visual.TextStim(win=win, name='rpK',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.08, wrapWidth=1000, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
rpL = visual.TextStim(win=win, name='rpL',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.08, wrapWidth=1000, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
rpM = visual.TextStim(win=win, name='rpM',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.08, wrapWidth=1000, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
regA = visual.Rect(
    win=win, name='regA',
    width=(1.0, 1.0)[0], height=(1.0, 1.0)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-12.0, interpolate=True)
regB = visual.Rect(
    win=win, name='regB',
    width=(1.0, 1.0)[0], height=(1.0, 1.0)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-13.0, interpolate=True)
regC = visual.Rect(
    win=win, name='regC',
    width=(1.0, 1.0)[0], height=(1.0, 1.0)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-14.0, interpolate=True)
regD = visual.Rect(
    win=win, name='regD',
    width=(1.0, 1.0)[0], height=(1.0, 1.0)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-15.0, interpolate=True)
regE = visual.Rect(
    win=win, name='regE',
    width=(1.0, 1.0)[0], height=(1.0, 1.0)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-16.0, interpolate=True)
regF = visual.Rect(
    win=win, name='regF',
    width=(1.0, 1.0)[0], height=(1.0, 1.0)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-17.0, interpolate=True)
regG = visual.Rect(
    win=win, name='regG',
    width=(1.0, 1.0)[0], height=(1.0, 1.0)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-18.0, interpolate=True)
regH = visual.Rect(
    win=win, name='regH',
    width=(1.0, 1.0)[0], height=(1.0, 1.0)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-19.0, interpolate=True)
regJ = visual.Rect(
    win=win, name='regJ',
    width=(1.0, 1.0)[0], height=(1.0, 1.0)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-20.0, interpolate=True)
regK = visual.Rect(
    win=win, name='regK',
    width=(1.0, 1.0)[0], height=(1.0, 1.0)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-21.0, interpolate=True)
regL = visual.Rect(
    win=win, name='regL',
    width=(1.0, 1.0)[0], height=(1.0, 1.0)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-22.0, interpolate=True)
regM = visual.Rect(
    win=win, name='regM',
    width=(1.0, 1.0)[0], height=(1.0, 1.0)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-23.0, interpolate=True)
tracks = sound.Sound('A', secs=-1, stereo=True)
tracks.setVolume(1)
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()

# Initialize components for Routine "Thanks"
ThanksClock = core.Clock()
Bye = visual.TextStim(win=win, name='Bye',
    text='Este es el final del tercer y último test.\n\n¡Muchas gracias por participar!\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1000, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Intro"-------
t = 0
IntroClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
IntroComponents = [Welcome, key_resp_2]
for thisComponent in IntroComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Intro"-------
while continueRoutine:
    # get current time
    t = IntroClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Welcome* updates
    if t >= 0.0 and Welcome.status == NOT_STARTED:
        # keep track of start time/frame for later
        Welcome.tStart = t
        Welcome.frameNStart = frameN  # exact frame index
        Welcome.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Intro"-------
for thisComponent in IntroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys=None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "Intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions_comprehension"-------
t = 0
Instructions_comprehensionClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()
# keep track of which components have finished
Instructions_comprehensionComponents = [text, key_resp_3]
for thisComponent in Instructions_comprehensionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instructions_comprehension"-------
while continueRoutine:
    # get current time
    t = Instructions_comprehensionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_3.keys = theseKeys[-1]  # just the last key pressed
            key_resp_3.rt = key_resp_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions_comprehensionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions_comprehension"-------
for thisComponent in Instructions_comprehensionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys=None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "Instructions_comprehension" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Comprehension = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('task_1.csv'),
    seed=None, name='Comprehension')
thisExp.addLoop(Comprehension)  # add the loop to the experiment
thisComprehension = Comprehension.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisComprehension.rgb)
if thisComprehension != None:
    for paramName in thisComprehension:
        exec('{} = thisComprehension[paramName]'.format(paramName))

for thisComprehension in Comprehension:
    currentLoop = Comprehension
    # abbreviate parameter names if possible (e.g. rgb = thisComprehension.rgb)
    if thisComprehension != None:
        for paramName in thisComprehension:
            exec('{} = thisComprehension[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "definition"-------
    t = 0
    definitionClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    sentences.setText(prompt)
    sentences.setFont('Calibri')
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    mouse.mouseClock.reset()
    resp_A.setText(respA)
    resp_B.setText(respB)
    resp_C.setText(respC)
    resp_D.setText(respD)
    key_resp_6 = event.BuilderKeyResponse()
    # keep track of which components have finished
    definitionComponents = [sentences, mouse, resp_A, resp_B, resp_C, resp_D, key_resp_6]
    for thisComponent in definitionComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "definition"-------
    while continueRoutine:
        # get current time
        t = definitionClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *sentences* updates
        if t >= 0.0 and sentences.status == NOT_STARTED:
            # keep track of start time/frame for later
            sentences.tStart = t
            sentences.frameNStart = frameN  # exact frame index
            sentences.setAutoDraw(True)
        # *mouse* updates
        if t >= 0.0 and mouse.status == NOT_STARTED:
            # keep track of start time/frame for later
            mouse.tStart = t
            mouse.frameNStart = frameN  # exact frame index
            mouse.status = STARTED
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [region_A,region_B,region_C,region_D]:
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    mouse.y.append(y)
                    buttons = mouse.getPressed()
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(mouse.mouseClock.getTime())
                    # abort routine on response
                    continueRoutine = False
        
        # *resp_A* updates
        if t >= 0.0 and resp_A.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp_A.tStart = t
            resp_A.frameNStart = frameN  # exact frame index
            resp_A.setAutoDraw(True)
        
        # *resp_B* updates
        if t >= 0.0 and resp_B.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp_B.tStart = t
            resp_B.frameNStart = frameN  # exact frame index
            resp_B.setAutoDraw(True)
        
        # *resp_C* updates
        if t >= 0.0 and resp_C.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp_C.tStart = t
            resp_C.frameNStart = frameN  # exact frame index
            resp_C.setAutoDraw(True)
        
        # *resp_D* updates
        if t >= 0.0 and resp_D.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp_D.tStart = t
            resp_D.frameNStart = frameN  # exact frame index
            resp_D.setAutoDraw(True)
        
        # *key_resp_6* updates
        if t >= 0.0 and key_resp_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_6.tStart = t
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_6.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_6.keys = theseKeys[-1]  # just the last key pressed
                key_resp_6.rt = key_resp_6.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in definitionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "definition"-------
    for thisComponent in definitionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for Comprehension (TrialHandler)
    if len(mouse.x): Comprehension.addData('mouse.x', mouse.x[0])
    if len(mouse.y): Comprehension.addData('mouse.y', mouse.y[0])
    if len(mouse.leftButton): Comprehension.addData('mouse.leftButton', mouse.leftButton[0])
    if len(mouse.midButton): Comprehension.addData('mouse.midButton', mouse.midButton[0])
    if len(mouse.rightButton): Comprehension.addData('mouse.rightButton', mouse.rightButton[0])
    if len(mouse.time): Comprehension.addData('mouse.time', mouse.time[0])
    if len(mouse.clicked_name): Comprehension.addData('mouse.clicked_name', mouse.clicked_name[0])
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys=None
    Comprehension.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        Comprehension.addData('key_resp_6.rt', key_resp_6.rt)
    # the Routine "definition" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'Comprehension'


# ------Prepare to start Routine "fin_1"-------
t = 0
fin_1Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
fin_1Components = [text_8]
for thisComponent in fin_1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "fin_1"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fin_1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_8* updates
    if t >= 0.0 and text_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_8.tStart = t
        text_8.frameNStart = frameN  # exact frame index
        text_8.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_8.status == STARTED and t >= frameRemains:
        text_8.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fin_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fin_1"-------
for thisComponent in fin_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "Instruction_English"-------
t = 0
Instruction_EnglishClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()
# keep track of which components have finished
Instruction_EnglishComponents = [text_2, key_resp_4]
for thisComponent in Instruction_EnglishComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instruction_English"-------
while continueRoutine:
    # get current time
    t = Instruction_EnglishClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_4.keys = theseKeys[-1]  # just the last key pressed
            key_resp_4.rt = key_resp_4.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instruction_EnglishComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruction_English"-------
for thisComponent in Instruction_EnglishComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys=None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.nextEntry()
# the Routine "Instruction_English" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
English = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('task_2.csv'),
    seed=None, name='English')
thisExp.addLoop(English)  # add the loop to the experiment
thisEnglish = English.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEnglish.rgb)
if thisEnglish != None:
    for paramName in thisEnglish:
        exec('{} = thisEnglish[paramName]'.format(paramName))

for thisEnglish in English:
    currentLoop = English
    # abbreviate parameter names if possible (e.g. rgb = thisEnglish.rgb)
    if thisEnglish != None:
        for paramName in thisEnglish:
            exec('{} = thisEnglish[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "expression"-------
    t = 0
    expressionClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    EN_exp.setPos((0, .5))
    EN_exp.setText(prompt)
    ans_A.setPos((0, .25))
    ans_A.setText(respA)
    reg_A.setOpacity(0)
    reg_A.setPos((0, .25))
    reg_A.setSize((0.6, 0.2))
    ans_B.setPos((0, 0))
    ans_B.setText(respB)
    reg_B.setOpacity(0)
    reg_B.setPos((0, 0))
    reg_B.setSize((0.6, 0.2))
    ans_C.setPos((0, -.25))
    ans_C.setText(respC)
    reg_C.setOpacity(0)
    reg_C.setPos((0, -.25))
    reg_C.setSize((0.6, 0.2))
    ans_D.setPos((0, -.5))
    ans_D.setText(respD)
    reg_D.setOpacity(0)
    reg_D.setPos((0, -.5))
    reg_D.setSize((0.6, 0.2))
    # setup some python lists for storing info about the mouse_2
    mouse_2.x = []
    mouse_2.y = []
    mouse_2.leftButton = []
    mouse_2.midButton = []
    mouse_2.rightButton = []
    mouse_2.time = []
    mouse_2.clicked_name = []
    gotValidClick = False  # until a click is received
    mouse_2.mouseClock.reset()
    
    # keep track of which components have finished
    expressionComponents = [EN_exp, ans_A, reg_A, ans_B, reg_B, ans_C, reg_C, ans_D, reg_D, mouse_2]
    for thisComponent in expressionComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "expression"-------
    while continueRoutine:
        # get current time
        t = expressionClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *EN_exp* updates
        if t >= 0.0 and EN_exp.status == NOT_STARTED:
            # keep track of start time/frame for later
            EN_exp.tStart = t
            EN_exp.frameNStart = frameN  # exact frame index
            EN_exp.setAutoDraw(True)
        
        # *ans_A* updates
        if t >= 0.0 and ans_A.status == NOT_STARTED:
            # keep track of start time/frame for later
            ans_A.tStart = t
            ans_A.frameNStart = frameN  # exact frame index
            ans_A.setAutoDraw(True)
        
        # *reg_A* updates
        if t >= 0.0 and reg_A.status == NOT_STARTED:
            # keep track of start time/frame for later
            reg_A.tStart = t
            reg_A.frameNStart = frameN  # exact frame index
            reg_A.setAutoDraw(True)
        
        # *ans_B* updates
        if t >= 0.0 and ans_B.status == NOT_STARTED:
            # keep track of start time/frame for later
            ans_B.tStart = t
            ans_B.frameNStart = frameN  # exact frame index
            ans_B.setAutoDraw(True)
        
        # *reg_B* updates
        if t >= 0.0 and reg_B.status == NOT_STARTED:
            # keep track of start time/frame for later
            reg_B.tStart = t
            reg_B.frameNStart = frameN  # exact frame index
            reg_B.setAutoDraw(True)
        
        # *ans_C* updates
        if t >= 0.0 and ans_C.status == NOT_STARTED:
            # keep track of start time/frame for later
            ans_C.tStart = t
            ans_C.frameNStart = frameN  # exact frame index
            ans_C.setAutoDraw(True)
        
        # *reg_C* updates
        if t >= 0.0 and reg_C.status == NOT_STARTED:
            # keep track of start time/frame for later
            reg_C.tStart = t
            reg_C.frameNStart = frameN  # exact frame index
            reg_C.setAutoDraw(True)
        
        # *ans_D* updates
        if t >= 0.0 and ans_D.status == NOT_STARTED:
            # keep track of start time/frame for later
            ans_D.tStart = t
            ans_D.frameNStart = frameN  # exact frame index
            ans_D.setAutoDraw(True)
        
        # *reg_D* updates
        if t >= 0.0 and reg_D.status == NOT_STARTED:
            # keep track of start time/frame for later
            reg_D.tStart = t
            reg_D.frameNStart = frameN  # exact frame index
            reg_D.setAutoDraw(True)
        # *mouse_2* updates
        if t >= 0.0 and mouse_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            mouse_2.tStart = t
            mouse_2.frameNStart = frameN  # exact frame index
            mouse_2.status = STARTED
            prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
        if mouse_2.status == STARTED:  # only update if started and not finished!
            buttons = mouse_2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [ans_A,ans_B,ans_C,ans_D]:
                        if obj.contains(mouse_2):
                            gotValidClick = True
                            mouse_2.clicked_name.append(obj.name)
                    x, y = mouse_2.getPos()
                    mouse_2.x.append(x)
                    mouse_2.y.append(y)
                    buttons = mouse_2.getPressed()
                    mouse_2.leftButton.append(buttons[0])
                    mouse_2.midButton.append(buttons[1])
                    mouse_2.rightButton.append(buttons[2])
                    mouse_2.time.append(mouse_2.mouseClock.getTime())
                    # abort routine on response
                    continueRoutine = False
        if mouse.isPressedIn(eval(correct)):
            corr = 1
        else:
            corr = 0
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in expressionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "expression"-------
    for thisComponent in expressionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for English (TrialHandler)
    if len(mouse_2.x): English.addData('mouse_2.x', mouse_2.x[0])
    if len(mouse_2.y): English.addData('mouse_2.y', mouse_2.y[0])
    if len(mouse_2.leftButton): English.addData('mouse_2.leftButton', mouse_2.leftButton[0])
    if len(mouse_2.midButton): English.addData('mouse_2.midButton', mouse_2.midButton[0])
    if len(mouse_2.rightButton): English.addData('mouse_2.rightButton', mouse_2.rightButton[0])
    if len(mouse_2.time): English.addData('mouse_2.time', mouse_2.time[0])
    if len(mouse_2.clicked_name): English.addData('mouse_2.clicked_name', mouse_2.clicked_name[0])
    
    # the Routine "expression" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'English'


# ------Prepare to start Routine "fin_2"-------
t = 0
fin_2Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
fin_2Components = [text_9]
for thisComponent in fin_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "fin_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fin_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_9* updates
    if t >= 0.0 and text_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_9.tStart = t
        text_9.frameNStart = frameN  # exact frame index
        text_9.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_9.status == STARTED and t >= frameRemains:
        text_9.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fin_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fin_2"-------
for thisComponent in fin_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "Instruction_knowledge"-------
t = 0
Instruction_knowledgeClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_5 = event.BuilderKeyResponse()
# keep track of which components have finished
Instruction_knowledgeComponents = [text_3, key_resp_5]
for thisComponent in Instruction_knowledgeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instruction_knowledge"-------
while continueRoutine:
    # get current time
    t = Instruction_knowledgeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    
    # *key_resp_5* updates
    if t >= 0.0 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_5.tStart = t
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_5.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_5.keys = theseKeys[-1]  # just the last key pressed
            key_resp_5.rt = key_resp_5.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instruction_knowledgeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruction_knowledge"-------
for thisComponent in Instruction_knowledgeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys=None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.nextEntry()
# the Routine "Instruction_knowledge" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "memory"-------
t = 0
memoryClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
text_4.setPos((-.65, 0))
text_4.setText('in cold blood\n\n\n\ntooth and nail\n\n\n\nbehind the scenes\n\n\n\nfrom the rooftops')
text_5.setText('for anything in the world\n\n\n\nnight and day\n\n\n\nby the sweat of his brow\n\n\n\nat the end of the day')
text_6.setPos((.65, 0))
text_6.setText("by any means\n\n\n\nwithin arm's reach\n\n\n\nto the letter\n\n\n\noff one's own bat")
key_resp_7 = event.BuilderKeyResponse()
# keep track of which components have finished
memoryComponents = [text_4, text_5, text_6, text_7, key_resp_7]
for thisComponent in memoryComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "memory"-------
while continueRoutine:
    # get current time
    t = memoryClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if t >= 0.0 and text_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_4.tStart = t
        text_4.frameNStart = frameN  # exact frame index
        text_4.setAutoDraw(True)
    
    # *text_5* updates
    if t >= 0.0 and text_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_5.tStart = t
        text_5.frameNStart = frameN  # exact frame index
        text_5.setAutoDraw(True)
    
    # *text_6* updates
    if t >= 0.0 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t
        text_6.frameNStart = frameN  # exact frame index
        text_6.setAutoDraw(True)
    
    # *text_7* updates
    if t >= 0.0 and text_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_7.tStart = t
        text_7.frameNStart = frameN  # exact frame index
        text_7.setAutoDraw(True)
    
    # *key_resp_7* updates
    if t >= 0.0 and key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_7.tStart = t
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_7.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in memoryComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "memory"-------
for thisComponent in memoryComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "memory" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Matching = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('task_3.csv'),
    seed=None, name='Matching')
thisExp.addLoop(Matching)  # add the loop to the experiment
thisMatching = Matching.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMatching.rgb)
if thisMatching != None:
    for paramName in thisMatching:
        exec('{} = thisMatching[paramName]'.format(paramName))

for thisMatching in Matching:
    currentLoop = Matching
    # abbreviate parameter names if possible (e.g. rgb = thisMatching.rgb)
    if thisMatching != None:
        for paramName in thisMatching:
            exec('{} = thisMatching[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "audio"-------
    t = 0
    audioClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    rpA.setPos((-.65, .6))
    rpA.setText(respA)
    rpB.setPos((-.65, .2))
    rpB.setText(respB)
    rpC.setPos((-.65, -.2))
    rpC.setText(respC)
    rpD.setPos((-.65, -.6))
    rpD.setText(respD)
    rpE.setPos((0, .6))
    rpE.setText(respE)
    rpF.setPos((0, .2))
    rpF.setText(respF)
    rpG.setPos((0, -.2))
    rpG.setText(respG)
    rpH.setPos((0, -.6))
    rpH.setText(respH)
    rpJ.setPos((.65, .6))
    rpJ.setText(respJ)
    rpK.setPos((.65, 0.2))
    rpK.setText(respK)
    rpL.setPos((.65, -.2))
    rpL.setText(respL)
    rpM.setPos((.65, -.6))
    rpM.setText(respM)
    regA.setOpacity(0)
    regA.setPos((-.65, 0.6))
    regA.setSize((0.6, 0.2))
    regB.setOpacity(0)
    regB.setPos((-.65, .2))
    regB.setSize((0.6, 0.2))
    regC.setOpacity(0)
    regC.setPos((-.65, -.2))
    regC.setSize((0.6, 0.2))
    regD.setOpacity(0)
    regD.setPos((-.65, -.6))
    regD.setSize((0.6, 0.2))
    regE.setOpacity(0)
    regE.setPos((0, .6))
    regE.setSize((0.6, 0.2))
    regF.setOpacity(0)
    regF.setPos((0, 0.2))
    regF.setSize((0.6, 0.2))
    regG.setOpacity(0)
    regG.setPos((0, -0.2))
    regG.setSize((0.6, 0.2))
    regH.setOpacity(0)
    regH.setPos((0, -0.6))
    regH.setSize((0.5, 0.2))
    regJ.setOpacity(0)
    regJ.setPos((.65, 0.6))
    regJ.setSize((0.6, 0.2))
    regK.setOpacity(0)
    regK.setPos((.65, 0.2))
    regK.setSize((0.6, 0.2))
    regL.setOpacity(0)
    regL.setPos((.65, -0.2))
    regL.setSize((0.6, 0.2))
    regM.setOpacity(0)
    regM.setPos((.65, -0.6))
    regM.setSize((0.6, 0.2))
    tracks.setSound(audio)
    tracks.setVolume(1, log=False)
    # setup some python lists for storing info about the mouse_3
    mouse_3.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    audioComponents = [rpA, rpB, rpC, rpD, rpE, rpF, rpG, rpH, rpJ, rpK, rpL, rpM, regA, regB, regC, regD, regE, regF, regG, regH, regJ, regK, regL, regM, tracks, mouse_3]
    for thisComponent in audioComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "audio"-------
    while continueRoutine:
        # get current time
        t = audioClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rpA* updates
        if t >= 0.0 and rpA.status == NOT_STARTED:
            # keep track of start time/frame for later
            rpA.tStart = t
            rpA.frameNStart = frameN  # exact frame index
            rpA.setAutoDraw(True)
        
        # *rpB* updates
        if t >= 0.0 and rpB.status == NOT_STARTED:
            # keep track of start time/frame for later
            rpB.tStart = t
            rpB.frameNStart = frameN  # exact frame index
            rpB.setAutoDraw(True)
        
        # *rpC* updates
        if t >= 0.0 and rpC.status == NOT_STARTED:
            # keep track of start time/frame for later
            rpC.tStart = t
            rpC.frameNStart = frameN  # exact frame index
            rpC.setAutoDraw(True)
        
        # *rpD* updates
        if t >= 0.0 and rpD.status == NOT_STARTED:
            # keep track of start time/frame for later
            rpD.tStart = t
            rpD.frameNStart = frameN  # exact frame index
            rpD.setAutoDraw(True)
        
        # *rpE* updates
        if t >= 0.0 and rpE.status == NOT_STARTED:
            # keep track of start time/frame for later
            rpE.tStart = t
            rpE.frameNStart = frameN  # exact frame index
            rpE.setAutoDraw(True)
        
        # *rpF* updates
        if t >= 0.0 and rpF.status == NOT_STARTED:
            # keep track of start time/frame for later
            rpF.tStart = t
            rpF.frameNStart = frameN  # exact frame index
            rpF.setAutoDraw(True)
        
        # *rpG* updates
        if t >= 0.0 and rpG.status == NOT_STARTED:
            # keep track of start time/frame for later
            rpG.tStart = t
            rpG.frameNStart = frameN  # exact frame index
            rpG.setAutoDraw(True)
        
        # *rpH* updates
        if t >= 0.0 and rpH.status == NOT_STARTED:
            # keep track of start time/frame for later
            rpH.tStart = t
            rpH.frameNStart = frameN  # exact frame index
            rpH.setAutoDraw(True)
        
        # *rpJ* updates
        if t >= 0.0 and rpJ.status == NOT_STARTED:
            # keep track of start time/frame for later
            rpJ.tStart = t
            rpJ.frameNStart = frameN  # exact frame index
            rpJ.setAutoDraw(True)
        
        # *rpK* updates
        if t >= 0.0 and rpK.status == NOT_STARTED:
            # keep track of start time/frame for later
            rpK.tStart = t
            rpK.frameNStart = frameN  # exact frame index
            rpK.setAutoDraw(True)
        
        # *rpL* updates
        if t >= 0.0 and rpL.status == NOT_STARTED:
            # keep track of start time/frame for later
            rpL.tStart = t
            rpL.frameNStart = frameN  # exact frame index
            rpL.setAutoDraw(True)
        
        # *rpM* updates
        if t >= 0.0 and rpM.status == NOT_STARTED:
            # keep track of start time/frame for later
            rpM.tStart = t
            rpM.frameNStart = frameN  # exact frame index
            rpM.setAutoDraw(True)
        
        # *regA* updates
        if t >= 0.0 and regA.status == NOT_STARTED:
            # keep track of start time/frame for later
            regA.tStart = t
            regA.frameNStart = frameN  # exact frame index
            regA.setAutoDraw(True)
        
        # *regB* updates
        if t >= 0.0 and regB.status == NOT_STARTED:
            # keep track of start time/frame for later
            regB.tStart = t
            regB.frameNStart = frameN  # exact frame index
            regB.setAutoDraw(True)
        
        # *regC* updates
        if t >= 0.0 and regC.status == NOT_STARTED:
            # keep track of start time/frame for later
            regC.tStart = t
            regC.frameNStart = frameN  # exact frame index
            regC.setAutoDraw(True)
        
        # *regD* updates
        if t >= 0.0 and regD.status == NOT_STARTED:
            # keep track of start time/frame for later
            regD.tStart = t
            regD.frameNStart = frameN  # exact frame index
            regD.setAutoDraw(True)
        
        # *regE* updates
        if t >= 0.0 and regE.status == NOT_STARTED:
            # keep track of start time/frame for later
            regE.tStart = t
            regE.frameNStart = frameN  # exact frame index
            regE.setAutoDraw(True)
        
        # *regF* updates
        if t >= 0.0 and regF.status == NOT_STARTED:
            # keep track of start time/frame for later
            regF.tStart = t
            regF.frameNStart = frameN  # exact frame index
            regF.setAutoDraw(True)
        
        # *regG* updates
        if t >= 0.0 and regG.status == NOT_STARTED:
            # keep track of start time/frame for later
            regG.tStart = t
            regG.frameNStart = frameN  # exact frame index
            regG.setAutoDraw(True)
        
        # *regH* updates
        if t >= 0.0 and regH.status == NOT_STARTED:
            # keep track of start time/frame for later
            regH.tStart = t
            regH.frameNStart = frameN  # exact frame index
            regH.setAutoDraw(True)
        
        # *regJ* updates
        if t >= 0.0 and regJ.status == NOT_STARTED:
            # keep track of start time/frame for later
            regJ.tStart = t
            regJ.frameNStart = frameN  # exact frame index
            regJ.setAutoDraw(True)
        
        # *regK* updates
        if t >= 0.0 and regK.status == NOT_STARTED:
            # keep track of start time/frame for later
            regK.tStart = t
            regK.frameNStart = frameN  # exact frame index
            regK.setAutoDraw(True)
        
        # *regL* updates
        if t >= 0.0 and regL.status == NOT_STARTED:
            # keep track of start time/frame for later
            regL.tStart = t
            regL.frameNStart = frameN  # exact frame index
            regL.setAutoDraw(True)
        
        # *regM* updates
        if t >= 0.0 and regM.status == NOT_STARTED:
            # keep track of start time/frame for later
            regM.tStart = t
            regM.frameNStart = frameN  # exact frame index
            regM.setAutoDraw(True)
        # start/stop tracks
        if t >= 0.0 and tracks.status == NOT_STARTED:
            # keep track of start time/frame for later
            tracks.tStart = t
            tracks.frameNStart = frameN  # exact frame index
            win.callOnFlip(tracks.play)  # screen flip
        # *mouse_3* updates
        if t >= 0.0 and mouse_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            mouse_3.tStart = t
            mouse_3.frameNStart = frameN  # exact frame index
            mouse_3.status = STARTED
            mouse_3.mouseClock.reset()
            prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
        if mouse_3.status == STARTED:  # only update if started and not finished!
            buttons = mouse_3.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [regA,regB,regC,regD,regE,regF,regG,regH,regJ,regK,regL,regM]:
                        if obj.contains(mouse_3):
                            gotValidClick = True
                            mouse_3.clicked_name.append(obj.name)
                    # abort routine on response
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in audioComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "audio"-------
    for thisComponent in audioComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    tracks.stop()  # ensure sound has stopped at end of routine
    # store data for Matching (TrialHandler)
    x, y = mouse_3.getPos()
    buttons = mouse_3.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        for obj in [regA,regB,regC,regD,regE,regF,regG,regH,regJ,regK,regL,regM]:
            if obj.contains(mouse_3):
                gotValidClick = True
                mouse_3.clicked_name.append(obj.name)
    Matching.addData('mouse_3.x', x)
    Matching.addData('mouse_3.y', y)
    Matching.addData('mouse_3.leftButton', buttons[0])
    Matching.addData('mouse_3.midButton', buttons[1])
    Matching.addData('mouse_3.rightButton', buttons[2])
    if len(mouse_3.clicked_name):
        Matching.addData('mouse_3.clicked_name', mouse_3.clicked_name[0])
    # the Routine "audio" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'Matching'


# ------Prepare to start Routine "Thanks"-------
t = 0
ThanksClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
ThanksComponents = [Bye]
for thisComponent in ThanksComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ThanksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Bye* updates
    if t >= 0.0 and Bye.status == NOT_STARTED:
        # keep track of start time/frame for later
        Bye.tStart = t
        Bye.frameNStart = frameN  # exact frame index
        Bye.setAutoDraw(True)
    frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if Bye.status == STARTED and t >= frameRemains:
        Bye.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ThanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Thanks"-------
for thisComponent in ThanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
