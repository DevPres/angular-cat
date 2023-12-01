def angular_magic_component_factory(input):
    return f'''
    This is the user request: '{input}'. 

    In the request there are some string delimited by single quotes, for example 'form'. this are magic keys
    In the request there is a string prefixed by -, for example -cat-pur. This is the magic name. If magic name is not present in the request, the magic name is ALWAYS cat-pur. if there are multiple name, take ONLY the first.
    In the request there is a string prefixed by --, for example --app. This is the prefix. If the  is not present in the request, the prefix is ALWAYS --app. If there are multiple name, take ONLY the first.

    the magic name capitalized is equl to the magic name but in PascalCase and ends with Component. example if magic name is cat-pur the magic name capitalized is CatPurComponent

    In the angular magic component there are string between single square, example [form]. this is the key. And string between double square, example [[import {{FormControl}} from '@angular/forms']]. this is the code.

    This is an example of angular magic components: 
    '
        import {{Component}} from '@angular/core'
        [form]
        [[import {{FormControl}} from '@angular/forms']] 

        @Component({{
            selector: '[prefix]-[magic name]',
            standalone: true,
            template: `
                <p>Meoow!<\p>
            `,
            styles: ``
        }})
        export class [magic name] {{
            [form]
            [[name = new FormControl('')]]
        }}
    '

    if in the magic keys there is the key 'form', the result should be:
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
    if in the magic keys there isn't the key 'form', the result should be:
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
    
    

    This is the angular magic component: {angular_magic_component}.
    '''


angular_magic_component = f'''
import {{Component [signal][[signal]]}} from '@angular/core'

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
    const cat: WritableSignal<string>=signal('meoow');
}}
'''