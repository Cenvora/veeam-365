from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rest_teams_team_fun_settings_giphy_content_rating import RESTTeamsTeamFunSettingsGiphyContentRating
from ..types import UNSET, Unset






T = TypeVar("T", bound="RESTTeamsTeamFunSettings")



@_attrs_define
class RESTTeamsTeamFunSettings:
    """ 
        Attributes:
            allow_custom_memes (bool | Unset): Defines whether users are allowed to include custom memes.
            allow_giphy (bool | Unset): Defines whether usage of Giphy is allowed.
            allow_stickers_and_memes (bool | Unset): Defines whether users are allowed to include stickers and memes.
            giphy_content_rating (RESTTeamsTeamFunSettingsGiphyContentRating | Unset): Giphy content rating.
     """

    allow_custom_memes: bool | Unset = UNSET
    allow_giphy: bool | Unset = UNSET
    allow_stickers_and_memes: bool | Unset = UNSET
    giphy_content_rating: RESTTeamsTeamFunSettingsGiphyContentRating | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        allow_custom_memes = self.allow_custom_memes

        allow_giphy = self.allow_giphy

        allow_stickers_and_memes = self.allow_stickers_and_memes

        giphy_content_rating: str | Unset = UNSET
        if not isinstance(self.giphy_content_rating, Unset):
            giphy_content_rating = self.giphy_content_rating.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if allow_custom_memes is not UNSET:
            field_dict["allowCustomMemes"] = allow_custom_memes
        if allow_giphy is not UNSET:
            field_dict["allowGiphy"] = allow_giphy
        if allow_stickers_and_memes is not UNSET:
            field_dict["allowStickersAndMemes"] = allow_stickers_and_memes
        if giphy_content_rating is not UNSET:
            field_dict["giphyContentRating"] = giphy_content_rating

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allow_custom_memes = d.pop("allowCustomMemes", UNSET)

        allow_giphy = d.pop("allowGiphy", UNSET)

        allow_stickers_and_memes = d.pop("allowStickersAndMemes", UNSET)

        _giphy_content_rating = d.pop("giphyContentRating", UNSET)
        giphy_content_rating: RESTTeamsTeamFunSettingsGiphyContentRating | Unset
        if isinstance(_giphy_content_rating,  Unset):
            giphy_content_rating = UNSET
        else:
            giphy_content_rating = RESTTeamsTeamFunSettingsGiphyContentRating(_giphy_content_rating)




        rest_teams_team_fun_settings = cls(
            allow_custom_memes=allow_custom_memes,
            allow_giphy=allow_giphy,
            allow_stickers_and_memes=allow_stickers_and_memes,
            giphy_content_rating=giphy_content_rating,
        )


        rest_teams_team_fun_settings.additional_properties = d
        return rest_teams_team_fun_settings

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
