# Switch (Toggle) Component - Alpine.js

## Installation

To use this component, you will need the pre-released Alpine UI plugin included via cdn. Make sure to include it BEFORE Alpine core JS file.

```html
<script defer src="https://unpkg.com/@alpinejs/ui@3.15.3/dist/cdn.min.js"></script>
<script defer src="https://unpkg.com/alpinejs@3.15.3/dist/cdn.min.js"></script>
```

## A Basic Example

```html
<div x-data="{ value: false }" x-switch:group>
    <label x-switch:label>Send notifications</label>

    <button x-switch x-model="value">
        <span :class="$switch.isChecked ? 'translate-x-7' : 'translate-x-1'"
              class="transition"
        ></span>
    </button>
</div>
```

## Styling based on the selected state

You can apply custom styling to the switch by using the $switch.isChecked boolean and setting any classes you need.

```html
<div x-switch:group>
    ...
    <button x-switch :class="$switch.isChecked ? 'checked' : 'not-checked'">
        ...
    </button>
</div>
```

## Specifying the default checked state

You can specify the default checked state when the page loads by using the default-checked attribute on the x-switch element.

```html
<div x-switch:group>
    ...
    <button x-switch default-checked>
        ...
    </button>
</div>
```

## Using as an HTML form input

If you are using the component inside a HTML form, you may pass a name prop to the x-switch element and Alpine will create a hidden input that is kept in sync with the value of the Switch.

If needed, you may also pass a value prop to the x-switch element and that will be sent as the value of the input when the form is submitted. The default value is "on" to mimic traditional checkboxes.

If no x-model is bound to the x-switch element, the component will manage its own state automatically.

```html
<div x-switch:group>
    ...
    <button x-switch name="enable_notifications" value="yes" class="...">
        ...
    </button>
</div>
```

## Keyboard Shortcuts

| Key | Description |
|-----|-------------|
| Space | Toggles the switch |

## API Reference

### x-switch

The main directive for the Switch component, used for the switch button.

| Attributes | Description |
|------------|-------------|
| x-model | Used to control the checked state using outside data |
| default-checked | A boolean to set the default checked state |
| name | Used to create a hidden input with the passed name that can be used for traditional HTML form submissions |
| value | Used in combination with name to set the checked value of the input |

### x-switch:group

Used to specify the group containing the switch button, label, and/or description.

### x-switch:label

Used to specify the label for the switch.

### x-switch:description

Used to specify an additional description for the switch.

### $switch

A magic variable that exposes information about the current state of the switch.

| Properties | Description |
|------------|-------------|
| isChecked | A boolean used to determine whether or not the switch is currently checked |