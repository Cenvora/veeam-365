from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_contact_item_actions import RESTContactItemActions
    from ..models.rest_contact_item_links import RESTContactItemLinks


T = TypeVar("T", bound="RESTContactItem")


@_attrs_define
class RESTContactItem:
    """
    Attributes:
        address (str | Unset): Contact address.
        business_phone (str | Unset): Business phone number of the contact.
        company (str | Unset): Company of the contact.
        display_as (str | Unset): Contact alias.
        email (str | Unset): Contact email.
        fax (str | Unset): Fax number of the contact.
        file_as (str | Unset): Name of the file.
        full_name (str | Unset): Contact full name.
        home_phone (str | Unset): Home phone number of the contact.
        im_address (str | Unset): Instant messenger address.
        job_title (str | Unset): Contact job title.
        mobile (str | Unset): Contact mobile.
        web_page (str | Unset): Contact webpage.
        item_class (str | Unset): Exchange item class.
        field_links (RESTContactItemLinks | Unset):
        field_actions (RESTContactItemActions | Unset):
        id (str | Unset): Exchange item ID.
    """

    address: str | Unset = UNSET
    business_phone: str | Unset = UNSET
    company: str | Unset = UNSET
    display_as: str | Unset = UNSET
    email: str | Unset = UNSET
    fax: str | Unset = UNSET
    file_as: str | Unset = UNSET
    full_name: str | Unset = UNSET
    home_phone: str | Unset = UNSET
    im_address: str | Unset = UNSET
    job_title: str | Unset = UNSET
    mobile: str | Unset = UNSET
    web_page: str | Unset = UNSET
    item_class: str | Unset = UNSET
    field_links: RESTContactItemLinks | Unset = UNSET
    field_actions: RESTContactItemActions | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        business_phone = self.business_phone

        company = self.company

        display_as = self.display_as

        email = self.email

        fax = self.fax

        file_as = self.file_as

        full_name = self.full_name

        home_phone = self.home_phone

        im_address = self.im_address

        job_title = self.job_title

        mobile = self.mobile

        web_page = self.web_page

        item_class = self.item_class

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_actions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_actions, Unset):
            field_actions = self.field_actions.to_dict()

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if business_phone is not UNSET:
            field_dict["businessPhone"] = business_phone
        if company is not UNSET:
            field_dict["company"] = company
        if display_as is not UNSET:
            field_dict["displayAs"] = display_as
        if email is not UNSET:
            field_dict["email"] = email
        if fax is not UNSET:
            field_dict["fax"] = fax
        if file_as is not UNSET:
            field_dict["fileAs"] = file_as
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if home_phone is not UNSET:
            field_dict["homePhone"] = home_phone
        if im_address is not UNSET:
            field_dict["imAddress"] = im_address
        if job_title is not UNSET:
            field_dict["jobTitle"] = job_title
        if mobile is not UNSET:
            field_dict["mobile"] = mobile
        if web_page is not UNSET:
            field_dict["webPage"] = web_page
        if item_class is not UNSET:
            field_dict["itemClass"] = item_class
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if field_actions is not UNSET:
            field_dict["_actions"] = field_actions
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_contact_item_actions import RESTContactItemActions
        from ..models.rest_contact_item_links import RESTContactItemLinks

        d = dict(src_dict)
        address = d.pop("address", UNSET)

        business_phone = d.pop("businessPhone", UNSET)

        company = d.pop("company", UNSET)

        display_as = d.pop("displayAs", UNSET)

        email = d.pop("email", UNSET)

        fax = d.pop("fax", UNSET)

        file_as = d.pop("fileAs", UNSET)

        full_name = d.pop("fullName", UNSET)

        home_phone = d.pop("homePhone", UNSET)

        im_address = d.pop("imAddress", UNSET)

        job_title = d.pop("jobTitle", UNSET)

        mobile = d.pop("mobile", UNSET)

        web_page = d.pop("webPage", UNSET)

        item_class = d.pop("itemClass", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTContactItemLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTContactItemLinks.from_dict(_field_links)

        _field_actions = d.pop("_actions", UNSET)
        field_actions: RESTContactItemActions | Unset
        if isinstance(_field_actions, Unset):
            field_actions = UNSET
        else:
            field_actions = RESTContactItemActions.from_dict(_field_actions)

        id = d.pop("id", UNSET)

        rest_contact_item = cls(
            address=address,
            business_phone=business_phone,
            company=company,
            display_as=display_as,
            email=email,
            fax=fax,
            file_as=file_as,
            full_name=full_name,
            home_phone=home_phone,
            im_address=im_address,
            job_title=job_title,
            mobile=mobile,
            web_page=web_page,
            item_class=item_class,
            field_links=field_links,
            field_actions=field_actions,
            id=id,
        )

        rest_contact_item.additional_properties = d
        return rest_contact_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
