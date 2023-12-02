def angular_magic_component_factory(input):
    return f'''
    This is the user request: '{input}'. 

    In the request there are strings that are keys. these are magick_keys. request example: 'generate angular component with keys: form,signal ....'. in this example form and signal are magic_keys.
    In the request there is a string that is the name. this is the magic_name. request example: 'generate angular component with name cat-template'. in this example cat-template is the magic_name. if there isn't a name the name is ALWAYS cat-template
    In the request there is a string that is the prefix. this is the magic_prefix. request example 'generate angular component with prefix app'. in this example app is the magic_prefix. if there isn't a prefix the prefix is ALWAYS app
    The magic_name_capitalized is equal to the magic name but in PascalCase and ends with Component. example if magic_name is cat-pur the magic_name_capitalized is CatPurComponent.

    In the angular_magic_component there are string between single square, example [form]. this is the key. And string between double square, example [[import {{FormControl}} from '@angular/forms']]. this is the code.
    If a key is among magic_keys, remove the key, and leave ONLY the code without square brackets.
    if a key isn't among magic_keys, remove the key and the code

    This is an example of angular_magic_components: 
    '
        import {{Component}} from '@angular/core'
        [form]
        [[import {{FormControl}} from '@angular/forms']] 

        @Component({{
            selector: '[prefix]-[magic_name]',
            standalone: true,
            template: `
                <p>Meoow!<\p>
            `,
            styles: ``
        }})
        export class [magic_name_capitalized] {{
            [form]
            [[purControl = new FormControl('')]]
            [meow]
            [i'm a cat]
        }}
    '

    if in the magic_keys there  is only key form, and the magic_name is 'cat' the result should be:
    '
        import {{Component}} from '@angular/core'
        import {{FormControl}} from '@angular/forms'

        @Component({{
            selector: 'app-cat-component',
            standalone: true,
            template: `
                <p>Meoow!<\p>
            `,
            styles: ``
        }})
        export class CatComponent {{
            purControl = new FormControl('')
        }}
    '
    if the magic_keys are empty, the result should be:
    '
        import {{Component}} from '@angular/core'

        @Component({{
            selector: 'app-cat-component',
            standalone: true,
            template: `
                <p>Meoow!<\p>
            `,
            styles: ``
        }})
        export class CatComponent {{}}
    '

    This is the angular_magic_component:
    '
        {angular_magic_component_template}.
    '

    answer with ONLY the angular_magic_component
    NEVER add code that is not in angular_magic_component
    '''


angular_magic_component_template = f'''
import {{Component [signal][[WritableSignal, signal]]}} from '@angular/core'
import {{[formControl][[FormControl]], [form][[FormGroup]]}} from '@angular/forms';

@Component({{
    selector: 'app-cat-component',
    standalone: true,
    template: `
        <p>Meoow!<\p>
    `,
    styles: ``
}})
export class CatComponent {{
    [signal]
    [[cat: WritableSignal<string>=signal('meoow');]]
    [formControl]
    [[catControl = new FormControl<any>('')]]
    [form]
    [[catGroup = new FormGroup<any>({{}})]]
}}
'''