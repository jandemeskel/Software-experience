#pragma once

#include <gl/freeglut.h>
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <vector>
#define _USE_MATH_DEFINES
#include <math.h>
#include <random>
#include <string>
#include <sstream>

#include "Window.h"
#include "rnd.h"

using namespace std;

// IsingSystem class
// this is where the Ising simulation happens
class IsingSystem {
private:
	Window *win;  // pointer to the window in which the system is running
				  // (this is not actually used but we keep it, just in case)

				  // size of grid: "static const" means that this number is a fixed constant
	static const int gridSize = 40;
	int **grid;  // this will be a 2d array that stores whether each site is occupied
	// random number generator, class name is rnd, instance is rgen
	rnd rgen;

	// this variable is 1 if the system is running, 0 for paused
	int isActive;

	// this variable is 1 if we are in "slow" mode, 0 in fast mode
	int slowNotFast;

	// this is the inverse temperature parameter beta
	double inverseTemperatureBeta;

public:
	// constructor
	IsingSystem(Window *set_win);
	// destructor
	~IsingSystem();

	// this sets the seed for the random numbers
	void setSeed(int s) { rgen.setSeed(s); }

	// these functions are used to update the system
	double computeLocalField(int pos[]);
	void attemptSpinFlip();
	void MCsweep();

	// increase or decrease the temperature (arbitrary increments)
	void Hotter() { inverseTemperatureBeta -= 0.025; }
	void Colder() { inverseTemperatureBeta += 0.025; }

	void setTemperature(double TTTT) { inverseTemperatureBeta = 1.0 / TTTT; }

	// set and read grid entries associated with a given position
	// NOTE! the grid is not accessed directly, only via these functions
	void setGrid(int pos[], int val);
	int readGrid(int pos[]);
	void flipSpin(int pos[]);


	// reset temperature to default value and re-initialise the grid
	void Reset();

	// "user interface" for the isActive variable
	int  isRunning() { return isActive; }
	void setRunning() { isActive = 1; }
	void pauseRunning() { isActive = 0; }

	// "user interface" for the slowNotFast variable
	int isSlow() { return slowNotFast; }
	void setSlow() { slowNotFast = 1; }
	void setFast() { slowNotFast = 0; }

	// set setpos to the position of a neighbour of pos
	// the neighbour to use is determined by val (=0,1,2,3)
	// beware: behavior is not defined for val>=4 or val<0
	void setPosNeighbour(int setpos[], int pos[], int val);

	// update the system: makes a Monte Carlo sweep
	void Update();

	// draws the system as squares
	void DrawSquares();

	void Netmag();  // function to calculate net magnetization 
	double M;   // Declaration of magnetisation varaible
	void DimE();
	double EJ;
	double RepeatNo = 1;
	static const int n0 = 150; // Number of MC sweeps to disregard (transient)
	static const int n = 10; // Number of MC sweeps 
	static const int m = 40; // Number of measurements per n MC sweeps
	static const int MCmax = (n0 + m * n + 1);
	int CurrentSweep;

	ofstream logfile1;
	ofstream logfile2;
	ofstream logfile3;

	// output file functions
	void openFile1(char name1[]) { logfile1.open(name1); }
	void closeFile1() { if (logfile1.is_open()) { logfile1.close(); } };
	void openFile2(char name2[]) { logfile2.open(name2); }
	void closeFile2() { if (logfile2.is_open()) { logfile2.close(); } };
	void openFile3(char name3[]) { logfile3.open(name3); }
	void closeFile3() { if (logfile3.is_open()) { logfile3.close(); } };

};
