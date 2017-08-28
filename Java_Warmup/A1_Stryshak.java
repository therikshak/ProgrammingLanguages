/**
* A!_Stryshak.java - a class for implementing warm-up functions
* @author Erik Stryshak
* @version 1.0
*/
import java.util.Random;
import java.util.Arrays;
class A1_Stryshak{
  public static void main(String[] args){
    /*SWAP TESTING*/
      int[] swapTestArray = {1,2,3,4,5,6};
      int[] expectedSwapArray = {6,2,3,4,5,1};
      swapTestArray = swap(swapTestArray, 0, 5);
      if(areEqualArrays(expectedSwapArray, swapTestArray)){
        System.out.println("swap : PASSED with " +
        Arrays.toString(swapTestArray));
      }
      else{
        System.out.println("swap : FAILED with " +
        Arrays.toString(swapTestArray));
      }

    /*SHUFFLE TESTING*/
      int[] shuffleTestArray = {45,32,12,6,532,31};
      int[] originalShuffleArray = {45,32,12,6,532,31};
      shuffleTestArray = shuffle(shuffleTestArray);
      if(areEqualArrays(shuffleTestArray, originalShuffleArray)){
        System.out.println("shuffle : FAILED with " +
        Arrays.toString(shuffleTestArray));
      }
      else{
        System.out.println("shuffle : PASSED with " +
        Arrays.toString(shuffleTestArray));
      }

    /*IS SORTED ARRAY*/
      int[] sortedArray = {1,2,3};
      boolean expected = true;
      boolean actual = isSortedArray(sortedArray);
      if(expected == actual){
        System.out.println("isSortedArray : PASSED with " +
        Arrays.toString(sortedArray));
      }
      else{
        System.out.println("isSortedArray : FAILED with " +
        Arrays.toString(sortedArray));
      }

      int[] unsortedArray={1,2,4,3};
      expected = false;
      actual = isSortedArray(unsortedArray);
      if(expected == actual){
        System.out.println("isSortedArray : PASSED with " +
        Arrays.toString(unsortedArray));
      }
      else{
        System.out.println("isSortedArray : FAILED with " +
        Arrays.toString(unsortedArray));
      }

    /*IS UNIQUE*/
      int[] uniqueArray = {1,2,3,4,5,6};
      expected = true;
      actual = isUniqueValuesArray(uniqueArray);
      if(expected == actual){
        System.out.println("isUniqueValuesArray : PASSED with " +
        Arrays.toString(uniqueArray));
      }
      else{
        System.out.println("isUniqueValuesArray : FAILED with " +
        Arrays.toString(uniqueArray));
      }

      int[] notUniqueArray = {1,2,3,4,3};
      expected = false;
      actual = isUniqueValuesArray(notUniqueArray);
      if(expected == actual){
        System.out.println("isUniqueValuesArray : PASSED with " +
        Arrays.toString(notUniqueArray));
      }
      else{
        System.out.println("isUniqueValuesArray : FAILED with " +
        Arrays.toString(notUniqueArray));
      }

    /*IS SORTED AND UNIQUE*/
      expected = true;
      actual = isSortedAndUniqueArray(uniqueArray);
      if(expected == actual){
        System.out.println("isSortedAndUniqueArray : PASSED with " +
        Arrays.toString(uniqueArray));
      }
      else{
        System.out.println("isSortedAndUniqueArray: FAILED with " +
        Arrays.toString(uniqueArray));
      }

      int[] notSortedUniqueArray = {3,4,5,9,12,10};
      expected = false;
      actual = isSortedAndUniqueArray(notSortedUniqueArray);
      if(expected == actual){
        System.out.println("isSortedAndUniqueArray : PASSED with " +
        Arrays.toString(notSortedUniqueArray));
      }
      else{
        System.out.println("isSortedAndUniqueArray: FAILED with " +
        Arrays.toString(notSortedUniqueArray));
      }

    /*GEN SORTED ARRAY UNIQUE VALUES*/
    int[] generatedArray = genSortedArrayUniqueValues(10);
    if(isSortedAndUniqueArray(generatedArray)){
      System.out.println("genSortedArrayUniqueValues : PASSED with " +
      Arrays.toString(generatedArray));
    }
    else{
      System.out.println("genSortedArrayUniqueValues: FAILED with " +
      Arrays.toString(generatedArray));
    }
  }

  public static int [] swap(int[] arr, int i, int j){
    /**
    * first checks to make sure both indices are in bounds, then
    * extracts the value at each index into variables and swaps them
    */
    if (i >= 0 && j >= 0 && i < arr.length && j <arr.length){
      int first_number = arr[i];
      int second_number = arr[j];
      arr[i] = second_number;
      arr[j] = first_number;
      return arr;
    }
    else{
      System.out.print("Out of bounds swap...returning original" +
      "array\n");
      return arr;
    }
  }

  public static int [] shuffle(int[] arr){
    /**
    * uses the Random library to generate a random_index
    * uses the user created swap function to swap the current index
    * and the randomly generated one
    */
    Random rand = new Random();
    int random_index = 0;
    for(int i=0; i<arr.length; i++){
      random_index = rand.nextInt(arr.length);
      arr = swap(arr, i, random_index);
    }
    return arr;
  }

  public static boolean isSortedArray(int[] arr){
    /**
    * loops through each value in the array and if the value is less
    * than value before it, returns false. If iterates through entire
    * array then it is sorted
    */
    for(int i=1; i<arr.length; i++){
      if(arr[i] < arr[i-1]){
        return false;
      }
    }
    return true;
  }

  public static boolean isSortedAndUniqueArray(int [] arr){
    /**
    * Uses the user-defined functions isSortedArray and
    * isUniqueValuesArray to determine if both criteria are met
    */
    if(isSortedArray(arr) && isUniqueValuesArray(arr)){
      return true;
    }
    return false;
  }

  public static boolean isUniqueValuesArray(int [] arr){
    /**
    * loops through each value in the array and compares it to each of
    * the other values
    */
    for(int i=0; i<arr.length-1; i++){
      for(int j=i+1; j<arr.length; j++){
        if(arr[i] == arr[j]){
          return false;
        }
      }
    }
    return true;
  }

  public static int [] genSortedArrayUniqueValues(int size){
    /**
    * uses the random library to generate a random size to increment
    * between 1 and 5. Creates an empty array of the specified size and
    * loops through each index, incrementing the value at the previous
    * index by the randomly generated increment
    */
    Random rand = new Random();
    int randomIncrement = 0;
    int[] arr = new int[size];
    arr[0] = rand.nextInt(5) + 1;
    for(int i=1; i<size; i++){
      randomIncrement = rand.nextInt(5) + 1;
      arr[i] = arr[i-1] + randomIncrement;
    }
    return arr;
  }

  public static boolean areEqualArrays(int[] arr1, int[] arr2){
    /**
    * tests if two arrays are equal
    * checks length first
    * then checks value at each index
    */
    if(arr1.length != arr2.length){
      return false;
    }
    for(int i=0; i<arr1.length; i++){
      if(arr1[i] != arr2[i]){
        return false;
      }
    }
    return true;
  }
}
