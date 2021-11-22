import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Random;

public class MyConnectFour {

  private BufferedReader input;
  private char[][] board;
  private Random rand;
  public MyConnectFour(){
    rand = new Random();
    board = new char[6][7];
    input = new BufferedReader(new InputStreamReader(System.in));
    playGame();
  }

  private void playGame(){
    System.out.println("Welcome to Connect 4");
    System.out.println("There are 2 players red and yellow");
    System.out.println("Player 1 is Red, Player 2 is Yellow");
    System.out.println("To play the game type in the number of the column you want to drop you counter in");
    System.out.println("A player wins by connecting 4 counters in a row - vertically, horizontally or diagonally");
    System.out.println("");
    printBoard();
    boolean win = false;
    boolean playerW = false;
    boolean compW = false;
    while(!win){
      String userInput = getUserInput();
      try{
        int move = Integer.parseInt(userInput) ;
        placeCounter('r',move);
      }
      catch(Exception e){
        System.out.println("Invalid input, insert integer between 1 and 7");
      }
      boolean hasWon = false;
      int count = 0;
      // check rows
      for(int i=0; i<board.length; i++){
        for(int j=0; j<board[i].length; j++){
          if(board[i][j] == 'r'){
            count = count + 1;
            if(count == 4){
              hasWon = true;
            }
          }
          else{
            count = 0;
          }
        }

      }
      // check columns
      for(int i=0; i<board[0].length; i++){
        for(int j=0; j<board.length; j++){
          if(board[j][i] == 'r'){
            count = count + 1;
            if(count == 4){
              hasWon = true;
            }
          }
          else{
            count = 0;
          }
        }
      }
      
      int currentLoopJ;
      // check diagonal, while moving along columns
      for(int j = 0; j<board[0].length; j++){
        currentLoopJ = j;
        for(int i = board.length -1 ; i>=0; i--){
            if(board[i][j] == 'r'){
              count = count + 1;
              j = j + 1;

              if(count == 4){
                hasWon = true;
                break;
              }
            }
            else{
              j = currentLoopJ;
              count = 0;
            }
          }
        }

      
      printBoard();
      if(hasWon){
        playerW = true;
        win = true;
      }

      else{
        try{
          int move = rand.nextInt(7)+1;
          placeCounter('y',move);
        }
        catch(Exception e){
          System.out.println("Invalid input, insert integer between 1 and 7");
          ;
        }
        hasWon = false;
        count = 0;
        // check horizontal
        for(int i=0; i<board.length; i++){
          for(int j=0; j<board[i].length; j++){
            if(board[i][j] == 'y'){
              count = count + 1;
              if(count == 4){
                hasWon = true;
              }
            }
            else{
              count = 0;
            }
          }
        }
        // check vertical
        count = 0;
        for(int i=0; i<board[0].length; i++){
          for(int j=0; j<board.length; j++){
            if(board[j][i] == 'y'){
              count = count + 1;
              if(count == 4){
                hasWon = true;
              }
            }
            else{
              count = 0;
            }
          }
        }
        printBoard();
        if(hasWon){
          compW = true;
          win = true;

        }
      }
    }
    if (playerW == true)
    {System.out.println("Well down, you have won.");}
    if (compW == true)
    {System.out.println("Unlucky, you have lost.");}
    System.out.println("Recompile if you would like to play again.");

  }

  private String getUserInput(){
    String toReturn = null;
    try{
       toReturn = input.readLine();
    }
    catch(Exception e){

    }
    return toReturn;
  }

  private void printBoard(){
    for( int i = 0; i<board.length ; i++){
      for(int j=0; j<board[i].length; j++){
        if(board[i][j] == 'r'){
          System.out.print("| r ");
        }
        else if(board[i][j] == 'y'){
          System.out.print("| y ");
        }
        else{
          System.out.print("|   ");
        }
      }
      System.out.println("|");
    }
    System.out.println("  1   2   3   4   5   6   7");
  }

  private void placeCounter(char player, int position){
    boolean placed = false;
    position = position-1;
    int counter = 0;
    while (placed == false && counter <=6 ){
    if(player == 'r'){
      for(int i=board.length-1  ; i >= 0; i--){
        if(!placed){
          if(board[i][position] == 'y' || board[i][position] == 'r' ){
            counter += 1;
          }
          else{
             board[i][position] = 'r';
            placed = true;
            
          }
          }
        }
    }
    else{
      for(int i=board.length-1  ; i >= 0; i--){
        if(!placed){
          if(board[i][position] == 'y' || board[i][position] == 'r' ){
            counter += 1;
          }
          else{
             board[i][position] = 'y';
            placed = true;
            
          }
          }
        }
      }
    }
    if(placed==false){
      System.out.println("You cannot place your counter in a full column");
    }
  }
 }