# HTML & CSS Notes

## HTML Basics
```html
<!DOCTYPE html>
<html>
  <head>
    <title>My Page</title>
  </head>
  <body>
    <h1>Hello World</h1>
    <p>This is a paragraph</p>
    <a href="https://github.com">GitHub</a>
    <img src="image.jpg" alt="My Image">
  </body>
</html>
```

## CSS Basics
```css
body {
  font-family: Arial;
  background-color: #f0f0f0;
}

h1 {
  color: blue;
  font-size: 32px;
}

p {
  margin: 10px;
  padding: 5px;
}
```

## CSS Flexbox
```css
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px;
}
```

## CSS Grid
```css
.container {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 10px;
}
```

## Useful CSS Properties
- color → text color
- background-color → background
- margin → outside spacing
- padding → inside spacing
- border → border around element
- border-radius → rounded corners
- font-size → text size
- font-weight → bold or normal