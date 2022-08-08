### CSS FlexBox

> display : flex 를 설정해 주면 코드의 자식 요소가 가로 정렬로 바뀌게 된다.
>
> 좀더 상세히 말하자면 수평된 주축을 기점으로 시작점에서 끝점 방향으로 자식요쇼들이 정렬하게 된다.
>
> 여기서 flex를 설정해준 코드는 `flex container`, 설정해준 코드의 자식 요소는 `flex items`로 불린다.

##### display : inline-flex

- `inline-flex`는 `flex container`를 block요소 처럼 세로로 쌓이는 것이 아닌 inline요소의 특징처럼 가로로 쌓이게 만든다.

  `display : flex`와의 차이점은 가로냐 세로냐 그정도 차이이다.

- `flex container`가 inline 요소처럼 정렬되는 것이고 그 안에 자식요소인 `flex items`와는 관계가 없다.

  

##### flex container, flex items에 적용가능한 속성

|      종류      | 사용 가능한 속성 |
| :------------: | :--------------: |
| flex container |    flex-flow     |
|                |  flex-direction  |
|                |    flex-wrap     |
|                | justify-content  |
|                |  align-content   |
|                |   align-items    |

|    종류    | 사용 가능한 속성 |
| :--------: | :--------------: |
| flex items |      order       |
|            |       flex       |
|            |    flex-grow     |
|            |   flex-shrink    |
|            |    flex-basis    |
|            |    align-self    |



##### justify-content

- 주 축의 정렬방법으로 기본 속성값은 `flex-start`이다.

- 주 축이 바뀌는 것이 아니기 때문에 `items`들의 순서는 바뀌지 않는다

- **justify-content 속성**

  |       flex-start        |       flex-end        |       center        |         space-between         |             space-around             |
  | :---------------------: | :-------------------: | :-----------------: | :---------------------------: | :----------------------------------: |
  | items를 시작점으로 정렬 | items를 끝점으로 정렬 | items를 가운데 정렬 | 각 items 사이를 균등하게 정렬 | 각 items의 외부 여백을 균등하게 정렬 |

  

##### align-content

- 교차축(수직)의 여러 줄 정렬 방법으로 기본 속성값은 `stretch`이다.

- `stretch`에서 `items`의 `height`값이 없다면 `items`들이 화면의 세로값을(height : auto) 꽉 채워서 출력이 된다.

- `align-content`는 `items`가 `flex-wrap:wrap`을 통해서 두 줄 이상일 때 작동을 한다.
  그리고 `flex container`안에 빈 여백이 있어야 작동한다.

- 여러 줄을 한 번에 정렬 시키기 용이하다.

- **align-content 속성**

  |         stretch         |        flex-star        |       flex-end        |         space-between         |             space-around             |
  | :---------------------: | :---------------------: | :-------------------: | :---------------------------: | :----------------------------------: |
  | items를 시작점으로 정렬 | items를 시작점으로 정렬 | items를 끝점으로 정렬 | 각 items 사이를 균등하게 정렬 | 각 items의 외부 여백을 균등하게 정렬 |

  

##### align-items

- 교차축(수직)의 한 줄 정렬 방법으로 기본 속성값은 `stretch`이다.

- 한 줄씩 정렬하는 방법이기 때문에 `flex-wrap:wrap`을 통하여 `items`가 여러 줄로 구성되었다면, 각 줄마다 시작점과 끝점이 존재하고 그 점을 기준으로 속성을 넣을 수 있다.

- `wrap` 적용 후 `align-items`를 사용했을 때 시작점과 끝점이 한 줄마다 생기는 화면

  ![image-20220809013109453](CSS_FlexBox.assets/image-20220809013109453.png)

- **align-items 속성**

  |         stretch         |        flex-star        |       flex-end        |       center        |                       baseline                       |
  | :---------------------: | :---------------------: | :-------------------: | :-----------------: | :--------------------------------------------------: |
  | items를 시작점으로 정렬 | items를 시작점으로 정렬 | items를 끝점으로 정렬 | items를 가운데 정렬 | 각 items 사이를 각 줄의 문자 기준선(baseline)에 정렬 |

  