use std::collections::HashMap;
use std::ops::Sub;
use std::fmt::Display;
use num_traits::identities::One;

fn fact<T>(x: T, memo: &mut HashMap<T, T>) -> T
where
    T: PartialOrd + PartialEq + One + Sub<Output = T> + Copy + Display,
{
    if x < T::one() {
        panic!("Invalid number: {}", x);
    } else if x.is_one() {
        return T::one();
    }

    if let Some(&result) = memo.get(&x) {
        return result;
    }

    let result = x * fact(x - T::one(), memo);
    memo.insert(x, result);
    result
}

fn main() {
    let mut memo: HashMap<u64, u64> = HashMap::new();
    println!("{}", fact(3u64, &mut memo));
}
