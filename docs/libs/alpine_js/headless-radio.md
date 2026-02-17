# Radio Component - Alpine.js

## Installation

To use this component, you will need the pre-released Alpine UI plugin included via cdn. Make sure to include it BEFORE Alpine core JS file.

```html
<script defer src="https://unpkg.com/@alpinejs/ui@3.15.3/dist/cdn.min.js"></script>
<script defer src="https://unpkg.com/@alpinejs/focus@3.15.3/dist/cdn.min.js"></script>
<script defer src="https://unpkg.com/alpinejs@3.15.3/dist/cdn.min.js"></script>
```

## A Basic Example

```html
<div x-data="{ framework: 'laravel' }">
    <div x-radio x-model="framework">
        <div x-radio:option value="laravel">
            <span :class="{ 'bg-blue-400': $radioOption.isChecked }">
                Laravel
            </span>
        </div>

        <div x-radio:option value="rails">
            <span :class="{ 'bg-blue-400': $radioOption.isChecked }">
                Ruby on Rails
            </span>
        </div>

        <div x-radio:option value="phoenix">
            <span :class="{ 'bg-blue-400': $radioOption.isChecked }">
                Phoenix
            </span>
        </div>
    </div>
</div>
```

## Styling active, checked, and disabled options

You can apply custom styling to active, checked, and disabled options by using the $radioOption.isActive, $radioOption.isChecked, and $radioOption.isDisabled booleans respectively and setting any classes you need.

```html
<div x-radio:option value="laravel">
    <span :class="{ 'bg-blue-400': $radioOption.isChecked }">
        Laravel
    </span>
</div>
```

## Disabling the radio

You can disable the radio group by adding the disabled attribute to a x-radio element.

```html
<div x-radio x-model="framework" disabled>
    ...
</div>
```

## Disabling an option

You can disable an option by adding the disabled attribute to a x-radio:option element. This will make this option un-selectable and will be skipped when navigating through options using the arrow-keys.

```html
<div x-radio:option value="laravel" disabled>
    ...
</div>
```

## Binding objects as values

Traditional HTML form inputs do not support using objects as values, but the x-radio component does.

```html
<div x-data="{
    framework: 'laravel',
    frameworks: [
        { id: 1, name: 'Laravel' },
        { id: 2, name: 'Ruby on Rails' },
        { id: 3, name: 'Phoenix' },
    ],
}">
    <div x-radio x-model="framework">
        <template x-for="item in frameworks" :key="item.id">
            <div x-radio:option :value="item">
                <span :class="{ 'bg-blue-400': $radioOption.isChecked }"
                      x-text="item.name"
                ></span>
            </div>
        </template>
    </div>
</div>
```

In order for the component to work correctly, ensure that you always use the same instance of the value objects, otherwise the component may not test equality correctly.

## Using as an HTML form input

If you are using the component inside an HTML form, you may pass a name prop to the x-radio element and Alpine will create a hidden input that is kept in sync with the value of the Radio.

If no x-model is bound to the x-radio element, the component will manage its own state automatically. In this case, you may pass a default-value prop to the x-radio element to specify which option should be checked when the page is initially loaded.

```html
<div x-radio name="framework">
    <div x-radio:option value="laravel">
        <span :class="{ 'bg-blue-400': $radioOption.isChecked }">
            Laravel
        </span>
    </div>
    ...
</div>
```

## Keyboard Shortcuts

| Key | Description |
|-----|-------------|
| Arrow Keys | Selects the next/previous non-disabled option |

## API Reference

### x-radio

The main directive for the Radio component, used to contain the behavior for a group of radio options.

| Attributes | Description |
|------------|-------------|
| x-model | Used to control which option is currently checked using outside data |
| name | Used to create a hidden input with the passed name that can be used for traditional HTML form submissions |
| default-value | A mixed value used to set the default checked option |
| disabled | A boolean used to disable the whole radio component |

### x-radio:option

Used to specify an individual option.

| Attributes | Description |
|------------|-------------|
| value | The value of the option |
| disabled | A boolean used to disable the option |

### $radioOption

A magic variable that exposes information about the current state of the option (element containing x-radio:option).

| Properties | Description |
|------------|-------------|
| isActive | A boolean used to determine whether or not an option is currently active |
| isChecked | A boolean used to determine whether or not an option is currently checked |
| isDisabled | A boolean used to determine whether or not an option is currently disabled |

### x-radio:label

Used to specify the label for an option or a group of options.

### x-radio:description

Used to specify the description for an option or a group of options.