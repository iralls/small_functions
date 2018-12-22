class ArrayExtras[A](a: Array[A]) {

  implicit def arrayExtras[A](a: Array[A]) = new ArrayExtras(a)

  def topN(sortBy: A => Int, n: Int = 2)(implicit tag: ClassTag[A]): Array[A] = {
    a
      .foldLeft(Array[A]()){ (x, y) =>
        x match {
          case d if d.length == 0 => Array(y)
          case d if d.length == 1 => Array(d(0), y)
          case d if d.length > 1 => (d :+ y).sortBy(f => -sortBy(f)).take(n)
        }
      }
  }

  def topNByKey(
    groupBy: A => String,
    sortBy: A => Int,
    n: Int = 2)(implicit tag: ClassTag[A]): Map[String, Array[A]] = {
    a
      .groupBy(groupBy)
      .mapValues(_.topN(sortBy, n))
  }
}
