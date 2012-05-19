<?php

/**
* Flatten an associative array into an array with indeces that are combinations of indeces of the original array separated by a delimeter, especially useful for json_encoded objects
*
* example: array(
*		'person' => array(
*			'age' => 50,
*			'height' => 5.7,
*			'interests' => array(
*					'sports',
*					'food'
*				),
*			'schoolstats' => array(
*					'name' => 'Some School',
*					'GPA' => 4.0
*				)
*			)
*		);
*
*print_r(flatten($array)) will print this:
*
*Array
*(
*    [person_age] => 50
*    [person_height] => 5.7
*    [person_interests_0] => sports
*    [person_interests_1] => food
*    [person_schoolstats_name] => Some School
*    [person_schoolstats_GPA] => 4
*)
*
*/

function flatten($array, $index_name = null, $return = array(), $original_array = null) {
	$delimeter = '_';
	if (!isset($original_array)) {
		$original_array = $array;
	}
	foreach ($array as $index => $value) {
		if (is_array($value)) {
			$return = flatten($value, isset($index_name) ? $index_name . '->' . $index : $index, $return, $original_array);
		} else {
			$name = isset($index_name) ? $index_name . '->' . $index : $index;
			$split = explode("->", $name);
			$new_array = $original_array;
			$line = null;
			foreach ($split as $array_index) {	
				$line .= isset($line) ? $delimeter . $array_index : $array_index;
				
				if (in_array($array_index, array_keys($new_array))) {
					if (isset($new_array[$array_index])) {
						$new_array = $new_array[$array_index];
					}
				} else {
					break;
				}
			}
			$return[$line] = isset($new_array) && !is_array($new_array) ? $new_array : null;
		}
	}
	return $return;
}
