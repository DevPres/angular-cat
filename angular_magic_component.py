def angular_magic_component_factory(input):
    return f'''
    This is the user request: '{input}'. 
    Answers ALWAYS following below instruction.

    instructions: 
    '
        {instructions}
    '

    This is the ANGULAR_MAGIC_COMPONENT:
    '
        {angular_magic_component_template}.
    '
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
    [ signal ]
    [[ cat: WritableSignal<string>=signal('meoow'); ]]
    [ formControl ]
    [[ catControl = new FormControl<any>(''); ]]
    [ form ]
    [[ catGroup = new FormGroup<any>({{}}); ]]
}}
'''

instructions='''
In the request there are strings that are keys. these are MAGIC_KEYS. request example: 'generate angular component with keys: form,signal ....'. in this example form and signal are MAGIC_KEYS.
In the request there is a string that is the name. this is the MAGIC_NAME. request example: 'generate angular component with name cat-template'. in this example cat-template is the MAGIC_NAME. if there isn't a name the name is ALWAYS cat-template
In the request there is a string that is the prefix. this is the PREFIX. request example 'generate angular component with prefix app'. in this example app is the PREFIX. if there isn't a PREFIX the PREFIX is ALWAYS app
The MAGIC_NAME_PASCAL_CASE is equal to the MAGIC_NAME but in PascalCase and ends with Component. example if MAGIC_NAME is cat-pur the MAGIC_NAME_PASCAL_CASE is CatPurComponent.

In the ANGULAR_MAGIC_COMPONENT there are string between single square, example [form]. these are the KEY. And string between double square, example [[import {FormControl} from '@angular/forms']]. these are the associated CODE.
If a key is among MAGIC_KEYS, remove the key, and leave ONLY the CODE WITHOUT square brackets.
if a key isn't among MAGIC_KEYS, remove the KEY and the CODE from ANGULAR_MAGIC_COMPONENT
NEVER add a message, but answers only with the ANGULAR_MAGIC_COMPONENT

This is an example of ANGULAR_MAGIC_COMPONENT: 
'
    import {Component} from '@angular/core'
    [ meow ]
    [[ import { mad cat } from '@everywhere' ]] 

    @Component({{
        selector: '[PREFIX]-[MAGIC_NAME]',
        standalone: true,
        template: `
            <p>Meoow!<\p>
        `,
        styles: ``
    }})
    export class [MAGIC_NAME_PASCAL_CASE] {{
        [ meow ]
        [[ i'm a cat ]]
    }}
'

if in the MAGIC_KEYS there is only key meow, and the MAGIC_NAME is 'cat' the answer should be:
'
    import {Component} from '@angular/core'
    import { cats } from '@everywhere'

    @Component({{
        selector: 'app-cat-component',
        standalone: true,
        template: `
            <p>Meoow!<\p>
        `,
        styles: ``
    }})
    export class CatComponent {{
        i'm a cat
    }}
'
if the MAGIC_KEYS are empty, the answer should be:
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

'''