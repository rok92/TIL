### Org JSON 파싱

> JSON이란?
> 
> Object, Array, Key-Value 형태로 이루어져 있으며 String, Int, Long, Boolean 등의 타입을 지원

##### Object

- Object는 {  }로 감싸여 있는 것을 말한다. 
  
  ```json
  {
    "title": "how to get stroage size",
    "url": "https://codechacha.com/ko/get-free-and-total-size-of-volumes-in-android/",
    "draft": false,
    "star": 10
  }
  ```

- 위의 JSON 코드에는 1개의 Object가 있고 그 안에 title, url, draft, star라는 4개의 key와 그에 해당하는 value를 가지고 있다.

##### Key-Value

- key-value는 위의 예제를 들면 "title"이 key, "how to get storage size"가 value에 해당 한다. key는 꼭 `"..."` 처럼 콜론으로 감싸져야 한다. value는 String 타입인 경우 `"..."`으로 표현하고 Boolean이나 Integer는 그냥 쓰면 된다.
  
  ```json
  "title": "how to get stroage size",
  ```


