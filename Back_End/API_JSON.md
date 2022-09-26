### API JSON 파싱

> **API**란, **Application Programming Interface**의 약자로, 응용 프로그램에서 사용할 수 있도록, 운영 체제나 프로그래밍 언어가 제공하는 기능을 제어할 수 있게 만든 인터페이스를 뜻한다
>
> **OPEN API**란, 사용자가 제공되는 데이터를 자유롭게 활용할 수 있도록 만들어놓은 인터페이스이다.
>
> 출처 : [open API 파싱하기(JSON) : 네이버 블로그 (naver.com)](https://blog.naver.com/PostView.naver?blogId=smj9030&logNo=222504396896&parentCategoryNo=&categoryNo=52&viewDate=&isShowPopularPosts=true&from=search)

##### API로 제공되어지는 형태는 대부분 `JSON`이나 `XML`로 제공이 된다.

- **XML**

  ```xml
  <response>
  	<header>
      	<resultCode>00</resultCode>
          <resultMsg>NOMAL_SERVICE</resultMsg>
      </header>
      <body>
      	<dataType>XML</dataType>
          <items>
          	<item>
              	<other>o 없음</other>
                  <t6>o 강풍주의보: 부산, 포항....</t6>
                  <t7>o 없음</t7>
                  <tmEf>202209130300</tmEf>
                  <tmFc>202209130000</tmFc>
                  <tmSeq>57</tmSeq>
              </item>
          </items>
          <numOfRows>10</numOfRows>
          <pageNo>1</pageNo>
          <totalCount>1</totalCount>
      </body>
  </response>
  ```

- **JSON**

  ```json
  {"bubbles":[{"data":{"description":"반려동물"},"type":"text"}],"event":"send","version":"v2","userId":"U47b00b58c90f8e47428af8b7bddc1231heo2","timestamp":1664104620182}
  ```

  - JSON이란 Javascript Object Notation의 약자로, key와 value로 이루어진 형태의 object이다.
  - 위의 코드 `"description":"반려동물"`에서 description는 key에 해당하고 반려동물은 value에 해당한다.

- **영화API를 통한 데이터 출력**

  - 먼저 데이터를 불러오기 위해서 사이트에서 제공 받은 API key를 key에 넣어준다. 

    그리고 웹페이지에 나온 JSON 결과값을 저장할 변수인 result를 선언해준다.

    ```java
    public class movieDetail {
    
    	public static void main(String[] args) {
    		String key = "f5eef3421c602c6cb7ea224104795888&movieCd=20124079";    
    		String result = "";
    		
    		try{
    			String apiURL = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key="
        				+ key + "&movieCd=20124039";
    			URL url = new URL(apiURL);
    			
    			BufferedReader bf;
    
    			bf = new BufferedReader(new InputStreamReader(url.openStream(), "UTF-8"));
    
    			result = bf.readLine();
    
    		}catch(Exception e){
    			e.printStackTrace();
    		}		
    	}
    }
    ```

    - 예외처리를 위해서 **try/catch** 를 처리해주고, String apiURL 변수에 **호출 URL**을 넣어준다. 

      **URL** 객체를 생성하고, new URL() 안에 apiURL을 넣어준다.

    - URL객체를 통해 url을 연결했으면, 원본 데이터를 가져와야 한다.

    - **BufferedReader**라는 속성에 Reader클래스가 오는데 URL에서 제공하는 메소드인 **openStream()**을 사용하기 위해서

      **InputStreamReader**를 속성으로 사용한다.

    - 읽어온 Buffer데이터를 readLine()메소드를 사용해서 한 줄씩 읽어 result변수에 저장한다.

  - **HttpURLConnection 객체 생성해서 url 연결**

    ```java
    public class movieDetail {
    
    	public static void main(String[] args) throws IOException {
    
    		String key = "f5eef3421c602c6cb7ea224104795888&movieCd=20124079";    
    
    		String result = "";
    
    		try {
    			String apiURL = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key="
        				+ key + "&movieCd=20124039";
    			URL url = new URL(apiURL);
    
    			HttpURLConnection con = (HttpURLConnection)url.openConnection();
    
    			//요청방식: POST
    			con.setRequestMethod("POST");
    			int responseCode = con.getResponseCode();
    
    			BufferedReader br;
    
    			if(responseCode==200) { // 정상 호출
    				br = new BufferedReader(new InputStreamReader(con.getInputStream()));
    			} else {  // 에러 발생
    				br = new BufferedReader(new InputStreamReader(con.getErrorStream()));
    			}
    
    			result = br.readLine();
    
    		} catch (Exception e) {
    			System.out.println(e);
    		}
    	}
    ```

    - HttpURLConnection은 http 통신을 수행할 객체이며, url 객체로 **connection**을 만들어 넣어준다. 
    - con.**setRequestMethod**("GET 또는 POST")메서드를 통해 요청방식을 정해준다.
    - http 요청 응답코드를 확인하는 responseCode의 값이 200이면 정상 호출로 getInputStream()메서드를 사용하여 데이터를 읽어온다.

  - **result값 JSON으로 변경**

    ```java
    JSONParser jsonParser = new JSONParser();
    JSONObject jsonObject = (JSONObject)jsonParser.parse(result);
    JSONObject movieInfoResult = (JSONObject)jsonObject.get("movieInfoResult");
    JSONObject movieInfo = (JSONObject)movieInfoResult.get("movieInfo");
    ```

    - JSONParser를 이용해서 String값을 JSON객체로 만들어 준다.

      이때, 만들어진 JSON객체는 JSONObject클래스를 사용해서 저장된다.

      만들어진 JSONObject에서 key가 movieInfoResult인 value를 추출하기 위해 get()을 사용한다.

      movieInfoResult에서 key가 movieInfo인 value를 JSONObject에 다시 넣어주면 된다.

  ![img](https://postfiles.pstatic.net/MjAyMTA5MTNfMjE1/MDAxNjMxNTE5MDc4NjI2.ZJp1r4Qqem-E2Shjyrticzrq5tHk3fReD_mw8wsL9Ncg.kSrloKjKGBJhnG3cEh5cVjOBt2HBn6s4v0lkgXjn-cUg.PNG.smj9030/image.png?type=w966)

  - 위 사진에서 key와 value안에 또다시 JSON이 존재하는 것을 확인할 수 있다.
  - nation이라는 key에 nationNm이라는 value가 JSON형태로 존재한다.
  - 이럴 때 JSONArray를 사용하여 내부 데이터를 Array로 바꿔주고 바뀐 Array안의 index마다 다시 JSONObject로 변환해 준다.