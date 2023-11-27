// move_semantics2.rs
//
// Make the test pass by finding a way to keep both Vecs separate!
//
// Execute `rustlings hint move_semantics2` or use the `hint` watch subcommand
// for a hint.

// Solution 1. clone when calling
#[test]
fn main() {
    let vec0 = vec![22, 44, 66];

    let mut vec1 = fill_vec(vec0.clone());

    assert_eq!(vec0, vec![22, 44, 66]);
    assert_eq!(vec1, vec![22, 44, 66, 88]);
}

fn fill_vec(mut vec: Vec<i32>) -> Vec<i32> {
    // let mut vec = vec;

    vec.push(88);

    vec
}

// Solution 2. clone at function using mutref
// #[test]
// fn main() {
//     let vec0 = vec![22, 44, 66];

//     let mut vec1 = fill_vec(&vec0);

//     assert_eq!(vec0, vec![22, 44, 66]);
//     assert_eq!(vec1, vec![22, 44, 66, 88]);
// }

// fn fill_vec(vec: &Vec<i32>) -> Vec<i32> {
//     let mut vec = vec.clone(); // Clone the input vector to make a mutable copy

//     vec.push(88); // Modify the mutable copy

//     vec // Return the modified copy
// }
