let bigInt = require("big-integer")

var test_monkey_obj = [
    {
        "starting_items": [79, 98],
        "operation": "* 19",
        "test_divisible": 23,
        "if_true_throw": 2,
        "if_false_throw": 3,
        "monkey_business": 0
    },
    {
        "starting_items": [54, 65, 75, 74],
        "operation": "+ 6",
        "test_divisible": 19,
        "if_true_throw": 2,
        "if_false_throw": 0,
        "monkey_business": 0
    },
    {
        "starting_items": [79, 60, 97],
        "worry_levels": [{}, {}, {}],
        "operation": "* old",
        "test_divisible": 13,
        "if_true_throw": 1,
        "if_false_throw": 3,
        "monkey_business": 0
    },
    {
        "starting_items": [74],
        "worry_levels": [{}],
        "operation": "+ 3",
        "test_divisible": 17,
        "if_true_throw": 0,
        "if_false_throw": 1,
        "monkey_business": 0
    },
]

test_monkey_obj = [
    {
        "starting_items": [bigInt(92), bigInt(73), bigInt(86), bigInt(83), bigInt(65), bigInt(51), bigInt(55), bigInt(93)],
        "operation": "* 5",
        "test_divisible": 11,
        "if_true_throw": 3,
        "if_false_throw": 4,
        "monkey_business": 0
    },
    {
        "starting_items": [bigInt(99), bigInt(67), bigInt(62), bigInt(61), bigInt(59), bigInt(98)],
        "operation": "* old",
        "test_divisible": 2,
        "if_true_throw": 6,
        "if_false_throw": 7,
        "monkey_business": 0
    },
    {
        "starting_items": [bigInt(81), bigInt(89), bigInt(56), bigInt(61), bigInt(99)],
        "operation": "* 7",
        "test_divisible": 5,
        "if_true_throw": 1,
        "if_false_throw": 5,
        "monkey_business": 0
    },
    {
        "starting_items": [bigInt(97), bigInt(74), bigInt(68)],
        "operation": "+ 1",
        "test_divisible": 17,
        "if_true_throw": 2,
        "if_false_throw": 5,
        "monkey_business": 0
    },
    {
        "starting_items": [bigInt(78), bigInt(73)],
        "operation": "+ 3",
        "test_divisible": 19,
        "if_true_throw": 2,
        "if_false_throw": 3,
        "monkey_business": 0
    },
    {
        "starting_items": [bigInt(50)],
        "operation": "+ 5",
        "test_divisible": 7,
        "if_true_throw": 1,
        "if_false_throw": 6,
        "monkey_business": 0
    },
    {
        "starting_items": [bigInt(95), bigInt(88), bigInt(53), bigInt(75)],
        "operation": "+ 8",
        "test_divisible": 3,
        "if_true_throw": 0,
        "if_false_throw": 7,
        "monkey_business": 0
    },
    {
        "starting_items": [bigInt(50), bigInt(77), bigInt(98), bigInt(85), bigInt(94), bigInt(56), bigInt(89)],
        "operation": "+ 2",
        "test_divisible": 13,
        "if_true_throw": 4,
        "if_false_throw": 0,
        "monkey_business": 0
    },
]



function run_first_problem(){
    monkey_num = test_monkey_obj.length
    
    // find level of monkey business after 20 rounds
    for(var round = bigInt(0); round < 10000; round++) {
        for(var monkey = 0; monkey < monkey_num; monkey++) {

            var starting_items = test_monkey_obj[monkey]["starting_items"]
            for(var item_ind = 0; item_ind < starting_items.length; item_ind++){
                item = bigInt(starting_items[item_ind])
                test_monkey_obj[monkey]["monkey_business"] = bigInt(test_monkey_obj[monkey]["monkey_business"]).add(1)
                operation = test_monkey_obj[monkey]["operation"]
                new_worry_level = bigInt(0)
                
                if(operation.includes("old")){
                    new_worry_level = item.pow(2, item)
                }
                else{
                    operation_array = operation.split(" ")
                    
                    operation_char = operation_array[0]
                    operation_number = bigInt(operation_array[1])
                    if (operation_char == "+"){
                        new_worry_level = item.add(bigInt(operation_number))
                    }
                    if (operation_char == "-"){
                        new_worry_level = item.sub(bigInt(operation_number))
                    }
                    if (operation_char == "*"){
                        new_worry_level = item.mul(bigInt(operation_number))
                    }
                }
                
                // new_worry_level = bigInt(Math.floor(new_worry_level / 3))
                if (!(bigInt(new_worry_level).mod(bigInt(test_monkey_obj[monkey]["test_divisible"])))){
                    throw_monkey_number = Number(test_monkey_obj[monkey]["if_true_throw"])
                    test_monkey_obj[throw_monkey_number]["starting_items"].push(bigInt(new_worry_level))
                }
                else{
                    throw_monkey_number = bigInt(test_monkey_obj[monkey]["if_false_throw"])
                    test_monkey_obj[throw_monkey_number]["starting_items"].push(bigInt(new_worry_level))
                }

                test_monkey_obj[monkey]["starting_items"] = []

                    
                // test_monkey_obj[monkey]["worry_levels"][item]["throw_monkey_number"] = throw_monkey_number
                // test_monkey_obj[monkey]["worry_levels"][item]["new_worry_level"] = new_worry_level
            }
            
        }
    }

    for (let item in test_monkey_obj){
        console.log(item)
        console.log(test_monkey_obj[item]["monkey_business"])
    }
    
}




run_first_problem()