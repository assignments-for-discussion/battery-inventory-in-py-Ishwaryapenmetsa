
def count_batteries_by_usage(cycles):
  batteryCount =  {
    "lowCount": 0,
    "mediumCount": 0,
    "highCount": 0
  }

  if isinstance(cycles, list): #Checking if data passed is valid or not
      for i in cycles:
        if i < 400 :
          batteryCount["lowCount"] = batteryCount["lowCount"]+1
        elif i >= 400 and i <= 919 :
          batteryCount["mediumCount"] = batteryCount["mediumCount"]+1
        else:
          batteryCount["highCount"] = batteryCount["highCount"]+1
  else:
    print("Invalid datatype") #printing error message for invalid data

  return batteryCount


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print("Done counting :)")

  counts = count_batteries_by_usage(None) #checking test case for none 
  assert(counts["lowCount"] == 0)
  assert(counts["mediumCount"] == 0)
  assert(counts["highCount"] == 0)

  counts = count_batteries_by_usage("Testing") #checking test case for invalid datatype (string)
  assert(counts["lowCount"] == 0)
  assert(counts["mediumCount"] == 0)
  assert(counts["highCount"] == 0)
   
  counts = count_batteries_by_usage(123) #checking test case for invalid datatype (int)
  assert(counts["lowCount"] == 0)
  assert(counts["mediumCount"] == 0)
  assert(counts["highCount"] == 0)


  counts = count_batteries_by_usage([919,400,350,920,1200]) #checking edge cases
  assert(counts["lowCount"] == 1)
  assert(counts["mediumCount"] == 2)
  assert(counts["highCount"] == 2)
  print("Done counting :)")





if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
