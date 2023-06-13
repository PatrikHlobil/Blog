---
date: 2023-06-12
categories: markdown
            presentation
---
# Marp: Markdown Presentation Ecosystem

## What is Marp?

!!! quote

    [Marp](https://marp.app/) (also known as the Markdown Presentation Ecosystem) provides an intuitive experience for creating beautiful slide decks. You only have to focus on writing your story in a Markdown document.

Here you find a few good references if you wish to get started using **Marp**:

- [https://marp.app/](https://marp.app/)
- [https://marpit.marp.app/](https://marpit.marp.app/)
- [https://chris-ayers.com/2023/03/31/customizing-marp](https://chris-ayers.com/2023/03/31/customizing-marp)
- [https://www.youtube.com/watch?v=EzQ-p41wNEE](https://www.youtube.com/watch?v=EzQ-p41wNEE)

## How to build a cool presentation

**Marp** is a really powerful tool to build an HTML presentation using Markdown. It can be developed inside VS Code (see e.g. https://www.youtube.com/watch?v=EzQ-p41wNEE) and the HTML can be directly exported there.

Let me give you an example presentation that shows how easy it is: 

<iframe src="../images/marp-presentation.html" title="Marp Presentation" width=800 height=600></iframe>

:material-presentation-play: [Marp Example Presenation](images/marp-presentation.html)

### Example:
~~~markdown 
---
paginate: true
marp: true
theme: uncover
class: invert
style: |
  .small-red-text {
    font-size: 0.75rem;
    color: red;
  }

  h1 {
    font-size: 60px;
  }

  h2 {
    font-size: 50px;
  } 
  
  h3 {
    font-size: 40px;
  }
  
  h4 {
    font-size: 30px;
  }

  h5,h6,p,li,code,table {
    font-size: 25px;
  }
headingDivider: 1
math: mathjax
---


# **Marp**


![bg left:40% 80%](https://marp.app/assets/marp.svg)

Markdown Presentation Ecosystem

https://marp.app/


# How to write slides

Split pages by horizontal ruler (`---`). It's very simple! :satisfied:

```markdown
# Slide 1

foobar


# Slide 2

foobar
```

Alternatively, set the **directive** [headingDivider](https://marpit.marp.app/directives?id=heading-divider). To automatically split at `h1` headers add to the document metadata:
```md
headingDivider: 1
```


# Markdown !!!

*Just* **write** `Markdown` ==here==!!!

- Bullet 1
- Bullet 2

### Subtitle

[Marp Link](https://marpit.marp.app/)

**Emojies**: :joy: :wink: :smile: :rocket:


# Markdown !!!
#### Use automatic syntax highlighting
```python
def foo(bar: str) -> str:
    return bar.strip()

if __name__ == "__main__":
    main()

```


# Markdown !!!

### Tables

| Syntax      | Description | Test Text     |
| :---        |    :----:   |          ---: |
| Header      | Title       | Here's this   |
| Paragraph   | Text        | And more      |


# Markdown !!!

## Crazy Math
<!-- _footer: You have to add **math: mathjax** to the document metadata -->
$$ 
f(a) = \frac{1}{2 \pi i} \oint_\gamma \frac{f(z)}{z-a} dz
$$


# Custom Backgrounds

![bg](https://image.slidesdocs.com/responsive-images/background/technology-clean-business-geometric-simple-blue-powerpoint-background_e3130f8dc2__960_540.jpg)

Use **Image Directives**:

```md
![bg](https://image.slidesdocs.com/responsive-images/background/
technology-clean-business-geometric-simple-blue-powerpoint-background_e3130f8dc2__960_540.jpg)

```


# Custom Backgrounds

![bg](https://media.istockphoto.com/id/517188688/photo/mountain-landscape.jpg?s=170667a&w=0&k=20&c=vKqLcyX0Qlrh8A351AA3-h2s5P46CZjh8JR6_QyV-D4=)

![bg](https://www.pexels.com/photo/2662116/download/)
**Multiple Backgrounds!!!**

```md
![bg](https://media.istockphoto.com/id/517188688/photo/mountain-landscape.jpg?s=170667a&w=0&k=20&c=vKqLcyX0Qlrh8A351AA3-h2s5P46CZjh8JR6_QyV-D4=)

![bg](https://www.pexels.com/photo/2662116/download/)
```


# Images

Put Images to the left

![bg left](https://www.pexels.com/photo/2662116/download/)
```md
![bg left](https://www.pexels.com/photo/2662116/download/)
```

# Images

... or to the right

![bg right](https://www.pexels.com/photo/2662116/download/)
```md
![bg right](https://www.pexels.com/photo/2662116/download/)
```

# Images

... or adjust the width ...

![bg left:25%](https://www.pexels.com/photo/2662116/download/)
```md
![bg left:25%](https://www.pexels.com/photo/2662116/download/)
```


# Images

... or apply filters:

![bg left sepia](https://www.pexels.com/photo/2662116/download/)
![bg right blur](https://www.pexels.com/photo/2662116/download/)
```md
![bg left sepia](https://www.pexels.com/photo/2662116/download/)
![bg right blur](https://www.pexels.com/photo/2662116/download/)
```


# GIFS !!!
```
![bg right](https://media2.giphy.com/media/1gXiBFTkANAddVgBKn/giphy.webp?cid=ecf05e47ar3gqt8z2h4b0n02u19dh257gwlwqge7zufd3sqd&ep=v1_gifs_search&rid=giphy.webp&ct=g)
![bg right](https://media0.giphy.com/media/SbtWGvMSmJIaV8faS8/200w.webp?cid=ecf05e47i5eyozrdt5aytc41m0o7ea6uxu6ck2088uxo4ojz&ep=v1_gifs_search&rid=200w.webp&ct=g)
```
![bg right](https://media2.giphy.com/media/1gXiBFTkANAddVgBKn/giphy.webp?cid=ecf05e47ar3gqt8z2h4b0n02u19dh257gwlwqge7zufd3sqd&ep=v1_gifs_search&rid=giphy.webp&ct=g)
![bg right](https://media0.giphy.com/media/SbtWGvMSmJIaV8faS8/200w.webp?cid=ecf05e47i5eyozrdt5aytc41m0o7ea6uxu6ck2088uxo4ojz&ep=v1_gifs_search&rid=200w.webp&ct=g)


# Mermaid Support

<!-- Add this anywhere in your Markdown file -->
<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true });
</script>

<div class="mermaid">
journey
    title My working day
    section Go to work
      Make tea: 5: Me
      Go upstairs: 3: Me
      Do work: 1: Me, Cat
    section Go home
      Go downstairs: 5: Me
      Sit down: 3: Me
</div>

# HTML Support

Add custom CSS to document metadata
```
---
marp: true
style: |
  .small-red-text {
    font-size: 0.75rem;
    color: red;
  }
---
# Title
<div class="small-red-text"> Small Red Text</div>
```


<div class="small-red-text"> Small Red Text</div>

# HTML Support

<div id="myDiv"> </div>
<script src='https://cdn.plot.ly/plotly-2.24.1.min.js'></script>
<script src='https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.17/d3.min.js'></script>

<script>
d3.json('https://raw.githubusercontent.com/plotly/plotly.js/master/test/image/mocks/sankey_energy.json', function(fig){

var data = {
  type: "sankey",
  domain: {
    x: [0,1],
    y: [0,1]
  },
  orientation: "h",
  valueformat: ".0f",
  valuesuffix: "TWh",
  node: {
    pad: 15,
    thickness: 15,
    line: {
      color: "black",
      width: 0.5
    },
   label: fig.data[0].node.label,
   color: fig.data[0].node.color
      },

  link: {
    source: fig.data[0].link.source,
    target: fig.data[0].link.target,
    value: fig.data[0].link.value,
    label: fig.data[0].link.label
  }
}

var data = [data]

var layout = {
  title: "Energy forecast for 2050<br>Source: Department of Energy & Climate Change, Tom Counsell via <a href='https://bost.ocks.org/mike/sankey/'>Mike Bostock</a>",
  width: 1000,
  height: 500,
  font: {
    size: 10
  }
}

Plotly.newPlot('myDiv', data, layout)
});

</script>


# Fragmented lists

Use `*` to get a fragmented list, where each item appears one after each other and `-` to directly display all items.

### Non-Fragmented

- non-frag 1
- non-frag 2

### Fragmented

* frag 1
* frag 2


# Speaker Notes

Just add **Speaker Notes** via:
```html
<!-- 
Some notes here that might be useful.
-->
```


<!-- 
Some notes here that might be useful.
-->

# Directives

<!-- _backgroundColor: #180f61 -->

With `Directives`, it is easy to modify the behaviour of **Marp** for a single slide or the whole presentation.

#### Local Directives

Using local directives (prepend with `_`), one can modify a single page, e.g.
```html
<!-- _backgroundColor: #180f61 -->
```

#### Global Directives

Using global directives, one can modify the bejaviour of the slides from the current slide on
```html
<!-- backgroundColor: aqua -->
```
~~~
